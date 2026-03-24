#!/usr/bin/env node
// build_npc_registry.js
//
// Generates editor/npc_registry.json by scanning:
//   - data/maps/<map>/map.json         (object_events -> appearances)
//   - data/maps/<map>/scripts.inc      (script -> trainer ID mapping)
//   - src/data/trainers.party          (trainer definitions)
//   - src/data/trainers_frlg.party     (FRLG trainer definitions)
//
// Usage:  node tools/data-manager/build_npc_registry.js

const fs = require('fs');
const path = require('path');

const ROOT = path.resolve(__dirname, '..', '..');

// ─── Trainer parser (reused from server.js) ─────────────────────────────────

function parseTrainers(content) {
    const trainers = [];
    const trainerBlocks = content.split(/^=== (TRAINER_\w+) ===/m);
    for (let i = 1; i < trainerBlocks.length; i += 2) {
        const trainerId = trainerBlocks[i].trim();
        const body = (trainerBlocks[i + 1] || '').trim();
        const trainer = { id: trainerId, pokemon: [] };
        const lines = body.split('\n');
        let currentMon = null;
        let pastTrainerFields = false;

        for (const rawLine of lines) {
            const line = rawLine.trim();
            if (!line || line.startsWith('/*') || line.startsWith('*/') || line.startsWith('//')) continue;

            if (!pastTrainerFields) {
                const fieldMatch = line.match(/^(Name|Class|Pic|Gender|Music|Double Battle|AI|Items|Mugshot|Starting Status):\s*(.*)$/i);
                if (fieldMatch) {
                    const key = fieldMatch[1].toLowerCase().replace(/\s+/g, '_');
                    trainer[key] = fieldMatch[2].trim();
                    continue;
                }
                pastTrainerFields = true;
            }

            const moveMatch = line.match(/^-\s+(.+)$/);
            if (moveMatch) {
                if (currentMon) {
                    if (!currentMon.moves) currentMon.moves = [];
                    currentMon.moves.push(moveMatch[1].trim());
                }
                continue;
            }

            const pokemonFieldMatch = line.match(/^(Level|Ability|Nature|IVs|EVs|Ball|Happiness|Shiny|Dynamax Level|Gigantamax|Tera Type):\s*(.*)$/i);
            if (pokemonFieldMatch) {
                if (currentMon) {
                    const key = pokemonFieldMatch[1].toLowerCase().replace(/\s+/g, '_');
                    currentMon[key] = pokemonFieldMatch[2].trim();
                }
                continue;
            }

            if (line && !line.startsWith('-')) {
                if (currentMon) trainer.pokemon.push(currentMon);
                currentMon = { species: line };
            }
        }
        if (currentMon) trainer.pokemon.push(currentMon);
        trainers.push(trainer);
    }
    return trainers;
}

// ─── Load all maps ──────────────────────────────────────────────────────────

function loadAllMaps() {
    const mapsDir = path.join(ROOT, 'data/maps');
    const mapFolders = fs.readdirSync(mapsDir).filter(f => {
        return fs.statSync(path.join(mapsDir, f)).isDirectory();
    });

    const maps = [];
    for (const folder of mapFolders) {
        const mapJsonPath = path.join(mapsDir, folder, 'map.json');
        if (!fs.existsSync(mapJsonPath)) continue;
        try {
            const mapData = JSON.parse(fs.readFileSync(mapJsonPath, 'utf-8'));
            mapData._folder = folder;
            maps.push(mapData);
        } catch { /* skip malformed */ }
    }
    return maps;
}

// ─── Parse scripts.inc for script→trainer mappings ──────────────────────────

function parseScriptTrainerLinks(mapFolder) {
    const scriptsPath = path.join(ROOT, 'data/maps', mapFolder, 'scripts.inc');
    if (!fs.existsSync(scriptsPath)) return {};

    const content = fs.readFileSync(scriptsPath, 'utf-8');
    const links = {}; // scriptLabel → [trainerIds]

    // Find each script label and its trainerbattle references
    const lines = content.split('\n');
    let currentScript = null;

    for (const line of lines) {
        const labelMatch = line.match(/^(\w+)::/);
        if (labelMatch) {
            currentScript = labelMatch[1];
        }

        if (currentScript) {
            const battleMatch = line.match(/trainerbattle_(?:single|double|rematch)\s+(TRAINER_\w+)/);
            if (battleMatch) {
                if (!links[currentScript]) links[currentScript] = [];
                if (!links[currentScript].includes(battleMatch[1])) {
                    links[currentScript].push(battleMatch[1]);
                }
            }
        }
    }

    return links;
}

// ─── Helpers ────────────────────────────────────────────────────────────────

function sanitizeId(str) {
    return str.toLowerCase().replace(/[^a-z0-9]+/g, '_').replace(/^_|_$/g, '');
}

function extractScriptStem(script) {
    if (!script || script === '0' || script === '0x0') return null;
    const parts = script.split('_EventScript_');
    if (parts.length >= 2) return parts[parts.length - 1];
    // Try other common patterns
    const commonParts = script.split('_EventScript');
    if (commonParts.length >= 2) return commonParts[commonParts.length - 1].replace(/^_/, '');
    return null;
}

function graphicsIdShort(gfxId) {
    return (gfxId || 'unknown')
        .replace('OBJ_EVENT_GFX_', '')
        .toLowerCase();
}

function titleCase(str) {
    return str.toLowerCase().replace(/\b\w/g, c => c.toUpperCase());
}

// ─── Main build ─────────────────────────────────────────────────────────────

function buildRegistry() {
    console.log('Loading maps...');
    const maps = loadAllMaps();
    console.log(`  Found ${maps.length} maps`);

    // Load trainers
    console.log('Loading trainers...');
    const allTrainers = [];
    for (const partyFile of ['src/data/trainers.party', 'src/data/trainers_frlg.party']) {
        const filePath = path.join(ROOT, partyFile);
        if (fs.existsSync(filePath)) {
            const content = fs.readFileSync(filePath, 'utf-8');
            const trainers = parseTrainers(content);
            for (const t of trainers) {
                t._sourceFile = partyFile;
            }
            allTrainers.push(...trainers);
        }
    }
    console.log(`  Found ${allTrainers.length} trainer entries`);

    // Build trainer lookup by ID
    const trainerById = {};
    for (const t of allTrainers) {
        trainerById[t.id] = t;
    }

    // Build script→trainer links for all maps
    console.log('Parsing scripts.inc files...');
    const scriptTrainerLinks = {}; // scriptLabel → [trainerIds]
    for (const map of maps) {
        const links = parseScriptTrainerLinks(map._folder);
        for (const [script, trainerIds] of Object.entries(links)) {
            scriptTrainerLinks[script] = trainerIds;
        }
    }

    // ── Build sprite_sets from unique graphics_ids ──────────────────────────
    console.log('Building sprite sets...');
    const graphicsIds = new Set();
    for (const map of maps) {
        for (const evt of (map.object_events || [])) {
            if (evt.graphics_id) graphicsIds.add(evt.graphics_id);
        }
    }

    const sprite_sets = {};
    for (const gfxId of graphicsIds) {
        const short = graphicsIdShort(gfxId);
        sprite_sets[short] = {
            id: short,
            label: short.replace(/_/g, ' ').replace(/\b\w/g, c => c.toUpperCase()),
            overworld_graphics_id: gfxId,
            trainer_pic: null,
            sprites: {}
        };
    }

    // ── Collect all object_events and link to trainers ──────────────────────
    console.log('Collecting object events and linking trainers...');
    const objectEvents = []; // enriched events with trainer links

    for (const map of maps) {
        for (const evt of (map.object_events || [])) {
            // Skip item balls and berry trees
            if ((evt.graphics_id || '').includes('ITEM_BALL')) continue;
            if ((evt.graphics_id || '').includes('BERRY_TREE')) continue;

            const enriched = {
                ...evt,
                _mapFolder: map._folder,
                _mapId: map.id,
                _mapName: map.name,
                _trainerIds: [],
            };

            // Link to trainers via scripts.inc
            if (evt.script && scriptTrainerLinks[evt.script]) {
                enriched._trainerIds = scriptTrainerLinks[evt.script];
            }

            objectEvents.push(enriched);
        }
    }
    console.log(`  Found ${objectEvents.length} object events (excluding items/berries)`);

    // ── Build NPC identities ────────────────────────────────────────────────
    console.log('Building NPC identities...');
    const npcs = {};
    const battles = {};
    const appearances = {};

    // Track which trainer IDs have been assigned to NPCs
    const trainerIdToNpcId = {};

    // 1) Trainer NPCs: group by Name + Class
    const trainerGroups = {}; // "class|name" → [trainers]
    for (const t of allTrainers) {
        const name = (t.name || '').trim();
        const cls = (t.class || 'PkMn Trainer').trim();
        if (!name) continue;
        const key = `${cls}|${name}`;
        if (!trainerGroups[key]) trainerGroups[key] = [];
        trainerGroups[key].push(t);
    }

    for (const [key, trainers] of Object.entries(trainerGroups)) {
        const [cls, name] = key.split('|');
        const npcId = sanitizeId(`${cls}_${name}`);

        // Find the sprite set from the first object_event that references any of these trainers
        let spriteSet = null;
        for (const evt of objectEvents) {
            if (evt._trainerIds.some(tid => trainers.some(t => t.id === tid))) {
                spriteSet = graphicsIdShort(evt.graphics_id);
                break;
            }
        }

        npcs[npcId] = {
            id: npcId,
            name: titleCase(name),
            class: cls,
            sprite_set: spriteSet,
            sprite_overrides: {},
            notes: ''
        };

        // Create battles for each trainer entry
        for (const t of trainers) {
            const battleId = sanitizeId(t.id);
            battles[battleId] = {
                id: battleId,
                npc_id: npcId,
                trainer_id: t.id,
                rematch_trainer_ids: [],
                double_battle: (t.double_battle || '').toLowerCase() === 'yes',
                notes: ''
            };
            trainerIdToNpcId[t.id] = npcId;
        }
    }

    // Detect rematch trainer IDs (e.g., TRAINER_TRENT_2 → rematch of TRAINER_TRENT_1)
    for (const [battleId, battle] of Object.entries(battles)) {
        const baseMatch = battle.trainer_id.match(/^(TRAINER_\w+?)_(\d+)$/);
        if (baseMatch) {
            const baseTrainer = baseMatch[1];
            const num = parseInt(baseMatch[2]);
            if (num > 1) {
                // This is a rematch — find the base battle
                const baseBattleId = sanitizeId(`${baseTrainer}_1`);
                if (battles[baseBattleId]) {
                    battles[baseBattleId].rematch_trainer_ids.push(battle.trainer_id);
                    // Remove this battle as standalone, it's a rematch
                    battle._isRematch = true;
                }
            }
        }
    }

    // Remove rematch battles from the top-level battles (they're referenced via rematch_trainer_ids)
    for (const [id, battle] of Object.entries(battles)) {
        if (battle._isRematch) {
            delete battles[id];
        }
    }
    // Clean up internal flags
    for (const battle of Object.values(battles)) {
        delete battle._isRematch;
    }

    // Build a lookup of trainer names (lowercase) to NPC IDs for name-matching
    const trainerNameToNpcId = {}; // lowercase name -> npcId
    for (const [key, trainers] of Object.entries(trainerGroups)) {
        const [cls, name] = key.split('|');
        const npcId = sanitizeId(`${cls}_${name}`);
        trainerNameToNpcId[name.toLowerCase()] = npcId;
    }

    // 2) Non-trainer NPCs: group by (graphics_id_short, script_stem)
    //    But first check if a script stem matches a known trainer name
    const nonTrainerGroups = {}; // "gfx_short|stem" -> [events]
    for (const evt of objectEvents) {
        if (evt._trainerIds.length > 0) continue; // Already handled as trainer
        const stem = extractScriptStem(evt.script);

        // Check if this non-trainer event's script stem matches a trainer name
        if (stem && trainerNameToNpcId[stem.toLowerCase()]) {
            evt._npcId = trainerNameToNpcId[stem.toLowerCase()];
            continue;
        }

        const gfxShort = graphicsIdShort(evt.graphics_id);
        const key = stem ? `${gfxShort}|${stem}` : `${gfxShort}|_anonymous_${evt._mapFolder}_${evt.x}_${evt.y}`;
        if (!nonTrainerGroups[key]) nonTrainerGroups[key] = [];
        nonTrainerGroups[key].push(evt);
    }

    for (const [key, events] of Object.entries(nonTrainerGroups)) {
        const [gfxShort, stem] = key.split('|');
        const npcId = sanitizeId(`${gfxShort}_${stem}`);

        // Avoid collision with trainer NPCs
        const finalId = npcs[npcId] ? `${npcId}_npc` : npcId;

        const label = stem.startsWith('_anonymous_')
            ? gfxShort.replace(/_/g, ' ').replace(/\b\w/g, c => c.toUpperCase())
            : stem.replace(/_/g, ' ').replace(/\b\w/g, c => c.toUpperCase());

        npcs[finalId] = {
            id: finalId,
            name: label,
            class: gfxShort.replace(/_/g, ' ').replace(/\b\w/g, c => c.toUpperCase()),
            sprite_set: gfxShort,
            sprite_overrides: {},
            notes: ''
        };

        // Store the event refs for appearance building
        for (const evt of events) {
            evt._npcId = finalId;
        }
    }

    // ── Build appearances ───────────────────────────────────────────────────
    console.log('Building appearances...');
    // Track appearance ID uniqueness
    const usedAppearanceIds = new Set();

    function makeAppearanceId(npcId, mapFolder) {
        let base = sanitizeId(`${npcId}_${mapFolder}`);
        if (!usedAppearanceIds.has(base)) {
            usedAppearanceIds.add(base);
            return base;
        }
        let counter = 2;
        while (usedAppearanceIds.has(`${base}_${counter}`)) counter++;
        const id = `${base}_${counter}`;
        usedAppearanceIds.add(id);
        return id;
    }

    for (const evt of objectEvents) {
        let npcId = null;
        let battleId = null;

        if (evt._trainerIds.length > 0) {
            // Trainer event — find the NPC via the first non-rematch trainer ID
            const primaryTrainerId = evt._trainerIds[0];
            npcId = trainerIdToNpcId[primaryTrainerId];

            // Find the matching battle
            const bId = sanitizeId(primaryTrainerId);
            if (battles[bId]) {
                battleId = bId;
            }
        } else if (evt._npcId) {
            npcId = evt._npcId;
        }

        if (!npcId) continue;

        const appId = makeAppearanceId(npcId, evt._mapFolder);

        appearances[appId] = {
            id: appId,
            npc_id: npcId,
            map: evt._mapFolder,
            map_id: evt._mapId || null,
            script: evt.script || null,
            position: { x: evt.x, y: evt.y },
            elevation: evt.elevation,
            movement_type: evt.movement_type || null,
            movement_range: { x: evt.movement_range_x || 0, y: evt.movement_range_y || 0 },
            trainer_type: evt.trainer_type || 'TRAINER_TYPE_NONE',
            battle_id: battleId,
            flag: evt.flag || '0'
        };
    }

    // ── Assemble and write ──────────────────────────────────────────────────
    const registry = {
        version: 1,
        sprite_sets,
        npcs,
        appearances,
        battles
    };

    const npcCount = Object.keys(npcs).length;
    const trainerNpcCount = Object.values(npcs).filter(n =>
        Object.values(battles).some(b => b.npc_id === n.id)
    ).length;
    const nonTrainerNpcCount = npcCount - trainerNpcCount;
    const appearanceCount = Object.keys(appearances).length;
    const battleCount = Object.keys(battles).length;
    const spriteSetCount = Object.keys(sprite_sets).length;

    console.log('\n── Registry Summary ──');
    console.log(`  Sprite sets:   ${spriteSetCount}`);
    console.log(`  NPCs:          ${npcCount} (${trainerNpcCount} trainers, ${nonTrainerNpcCount} non-trainers)`);
    console.log(`  Appearances:   ${appearanceCount}`);
    console.log(`  Battles:       ${battleCount}`);

    const outPath = path.join(ROOT, 'editor/npc_registry.json');
    fs.writeFileSync(outPath, JSON.stringify(registry, null, 2));
    console.log(`\nWritten to: ${outPath}`);

    return registry;
}

// Allow both CLI execution and require() for use in server.js
if (require.main === module) {
    buildRegistry();
}

module.exports = { buildRegistry, parseTrainers };
