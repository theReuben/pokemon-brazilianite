# Headless GBA screenshots

Renders frames from the built ROM without opening an emulator window. Used when a
UI change needs eyeballing.

- `driver.c` - links Homebrew's `libmgba`, runs the ROM headless, feeds a scripted
  key sequence and dumps raw RGBA frames.
  `cc -O2 -I/opt/homebrew/include -L/opt/homebrew/lib -lmgba -o driver driver.c`
- `drive.py` - press/screenshot plans; edit `S` to point at the ROM copy.
- `topng.py` - raw frame -> PNG, with an integer zoom for inspecting sprites.
  The framebuffer is BGRA, so pass `bgr`.

Notes:
- `tools/mgba/mgba-rom-test-mac` advertises `--script` but was built without Lua,
  so it can't drive the ROM.
- `DebugPrintf` needs `gmake DEBUG_LOGGING=1`, and `src/main.c` must be rebuilt too
  or the `MgbaOpen()` handshake is compiled out and nothing prints.
- The repo's `pokeemerald.sav` is blank, so reaching a menu means either playing
  through it or temporarily pointing `InitMainCallbacks` at a CB2 that calls
  `NewGameInitData()`, builds a party and jumps straight to the screen.
