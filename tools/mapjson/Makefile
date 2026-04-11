CXX ?= g++
CXXFLAGS := -Wall -std=c++17 -O2

ifeq ($(shell uname),Darwin)
# Use Apple's clang++ from the Xcode toolchain (full path bypasses Homebrew)
MACOS_CXX := $(shell xcrun --find clang++ 2>/dev/null)
ifneq ($(MACOS_CXX),)
CXX := $(MACOS_CXX)
endif
# Export SDKROOT so clang++ can locate C and C++ stdlib headers
export SDKROOT ?= $(shell xcrun --sdk macosx --show-sdk-path 2>/dev/null)
endif

SRCS := json11.cpp mapjson.cpp

HEADERS := mapjson.h

ifeq ($(OS),Windows_NT)
EXE := .exe
else
EXE :=
endif

.PHONY: all clean

all: mapjson$(EXE)
	@:

mapjson$(EXE): $(SRCS) $(HEADERS)
	$(CXX) $(CXXFLAGS) $(SRCS) -o $@ $(LDFLAGS)

clean:
	$(RM) mapjson mapjson.exe
