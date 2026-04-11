CXX ?= g++
CXXFLAGS = -Wall -Werror -std=c++11 -O2

ifeq ($(shell uname),Darwin)
# Use Apple's clang++ from the Xcode toolchain (full path bypasses Homebrew)
MACOS_CXX := $(shell xcrun --find clang++ 2>/dev/null)
ifneq ($(MACOS_CXX),)
CXX := $(MACOS_CXX)
endif
# Export SDKROOT so clang++ can locate C and C++ stdlib headers
export SDKROOT ?= $(shell xcrun --sdk macosx --show-sdk-path 2>/dev/null)
endif

SRCS = scaninc.cpp c_file.cpp asm_file.cpp source_file.cpp

HEADERS := scaninc.h asm_file.h c_file.h source_file.h

.PHONY: all clean

ifeq ($(OS),Windows_NT)
EXE := .exe
else
EXE :=
endif

all: scaninc$(EXE)
	@:

scaninc$(EXE): $(SRCS) $(HEADERS)
	$(CXX) $(CXXFLAGS) $(SRCS) -o $@ $(LDFLAGS)

clean:
	$(RM) scaninc scaninc.exe
