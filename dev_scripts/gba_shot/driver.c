// Headless mGBA driver: runs the ROM, feeds a scripted key sequence, dumps raw frames.
#include <mgba/core/core.h>
#include <mgba/core/config.h>
#include <mgba/gba/core.h>
#include <mgba-util/vfs.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

static uint32_t videoBuffer[240 * 160];

int main(int argc, char** argv) {
    const char* rom = argv[1];
    const char* save = argv[2];
    const char* outdir = argv[3];

    struct mCore* core = mCoreFind(rom);
    if (!core) { fprintf(stderr, "no core\n"); return 1; }
    if (!core->init(core)) { fprintf(stderr, "init failed\n"); return 1; }
    mCoreInitConfig(core, NULL);

    unsigned w, h;
    core->desiredVideoDimensions(core, &w, &h);
    fprintf(stderr, "dims %ux%u\n", w, h);
    core->setVideoBuffer(core, videoBuffer, w);
    core->setAudioBufferSize(core, 2048);

    if (!mCoreLoadFile(core, rom)) { fprintf(stderr, "rom load failed\n"); return 1; }
    struct VFile* sav = VFileOpen(save, O_RDWR);
    if (sav && !core->loadSave(core, sav)) fprintf(stderr, "save load failed\n");
    core->reset(core);

    int maxFrame = 0;
    for (int i = 4; i < argc; i++) {
        int f = atoi(argv[i] + (argv[i][0] == 'S' ? 2 : 0));
        if (f > maxFrame) maxFrame = f;
    }

    for (int frame = 0; frame <= maxFrame; frame++) {
        uint32_t keys = 0;
        for (int i = 4; i < argc; i++) {
            if (argv[i][0] == 'S') continue;
            int f; unsigned k;
            if (sscanf(argv[i], "%d:%x", &f, &k) == 2 && f == frame) keys |= k;
        }
        core->setKeys(core, keys);
        core->runFrame(core);
        for (int i = 4; i < argc; i++) {
            if (argv[i][0] != 'S') continue;
            if (atoi(argv[i] + 2) != frame) continue;
            char path[512];
            snprintf(path, sizeof(path), "%s/frame_%05d.raw", outdir, frame);
            FILE* fp = fopen(path, "wb");
            fwrite(videoBuffer, 4, 240 * 160, fp);
            fclose(fp);
            printf("dumped frame %d\n", frame);
        }
    }
    return 0;
}
