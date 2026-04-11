CXX ?= g++
CXXFLAGS := -std=c++11 -O2 -Wall -Wno-switch -Werror

ifeq ($(shell uname),Darwin)
# Use Apple's clang++ from the Xcode toolchain (full path bypasses Homebrew)
MACOS_CXX := $(shell xcrun --find clang++ 2>/dev/null)
ifneq ($(MACOS_CXX),)
CXX := $(MACOS_CXX)
endif
# Export SDKROOT so clang++ can locate C and C++ stdlib headers
export SDKROOT ?= $(shell xcrun --sdk macosx --show-sdk-path 2>/dev/null)
endif

SRCS := asm_file.cpp c_file.cpp charmap.cpp preproc.cpp string_parser.cpp \
	utf8.cpp io.cpp

HEADERS := asm_file.h c_file.h char_util.h charmap.h preproc.h string_parser.h \
	utf8.h io.h

ifeq ($(OS),Windows_NT)
EXE := .exe
else
EXE :=
endif

.PHONY: all clean

all: preproc$(EXE)
	@:

preproc$(EXE): $(SRCS) $(HEADERS)
	$(CXX) $(CXXFLAGS) $(SRCS) -o $@ $(LDFLAGS)

clean:
	$(RM) preproc preproc.exe
