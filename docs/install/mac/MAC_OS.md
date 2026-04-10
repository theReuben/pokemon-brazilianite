# Instructions for macOS

## Required Dependencies

The following tools are **all required** to build the ROM:

| Tool | Provides | Install Method |
|------|----------|---------------|
| Xcode Command Line Tools | Basic build tools (`gcc`, `make`) | `xcode-select --install` |
| libpng | PNG image processing (`png.h`) | `brew install libpng` |
| pkg-config | Library detection for libpng | `brew install pkg-config` |
| devkitARM | ARM cross-compiler (`arm-none-eabi-gcc`) | See [Installing devkitARM](#installing-devkitarm-macos) |
| Python 3 | Build scripts | [python.org](https://www.python.org/downloads/) or `brew install python` |

> **Common build errors and their causes:**
> - `arm-none-eabi-gcc: command not found` → devkitARM is not installed or not in PATH
> - `pkg-config: Command not found` → pkg-config is not installed
> - `'png.h' file not found` → libpng is not installed

## Step-by-step Setup

1. If the Xcode Command Line Tools are not installed, download the tools [here](https://developer.apple.com/xcode/resources/), open your Terminal, and run the following command:

    ```bash
    xcode-select --install
    ```

2. Install [Homebrew](https://brew.sh/) if not already installed:

    ```bash
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
    ```

3. Install libpng and pkg-config via Homebrew:

    ```bash
    brew install libpng pkg-config
    ```

4. Install devkitARM — see [Installing devkitARM (macOS)](#installing-devkitarm-macos) below.

5. **Optional: To run tests**, install coreutils:

    ```bash
    brew install coreutils
    ```

6. **Optional: To run tests via Rosetta**
    - You probably don't want to do this as it's much slower. Most users can use native tools, but some may have other reasons to use this setup such as working with Intel-only custom tooling.
    - You will need an Intel-compatible homebrew installation. Understanding how to get one can be found [here](https://github.com/Homebrew/brew/issues/9173#issuecomment-729206868).
    - Install `coreutils` like in step 5, but using your Intel-compatible installation of homebrew.

### Installing devkitARM (macOS)
1. Download the `devkitpro-pacman-installer.pkg` package from [here](https://github.com/devkitPro/pacman/releases).
2. Open the package to install devkitPro pacman.
3. In the Terminal, run the following commands to install devkitARM:

    ```bash
    sudo dkp-pacman -Sy
    sudo dkp-pacman -S gba-dev
    sudo dkp-pacman -S devkitarm-rules
    ```

    The command with gba-dev will ask for the selection of packages to install. Just press Enter to install all of them, followed by entering Y to proceed with the installation.

4. After the tools are installed, devkitARM must now be made accessible from anywhere by the system. To do so, run the following commands:

    ```bash
    export DEVKITPRO=/opt/devkitpro
    echo "export DEVKITPRO=$DEVKITPRO" >> ~/.zshrc
    export DEVKITARM=$DEVKITPRO/devkitARM
    echo "export DEVKITARM=$DEVKITARM" >> ~/.zshrc

    echo "if [ -f ~/.zshrc ]; then . ~/.zshrc; fi" >> ~/.zprofile
    ```
    *Note: Starting with macOS 10.15, the default Unix shell is now zsh. If you migrated from an older version of macOS, you might still be using bash. You can check by running `echo $0` in the terminal.*
    <details>
        <summary><i>If your terminal is using bash instead of zsh...</i></summary>

    ```bash
    export DEVKITPRO=/opt/devkitpro
    echo "export DEVKITPRO=$DEVKITPRO" >> ~/.bashrc
    export DEVKITARM=$DEVKITPRO/devkitARM
    echo "export DEVKITARM=$DEVKITARM" >> ~/.bashrc

    echo "if [ -f ~/.bashrc ]; then . ~/.bashrc; fi" >> ~/.bash_profile
    ```
    </details>

### Installing Python (macOS)
1. Download the latest Python package from [here](https://www.python.org/downloads/).
2. Open the package to install Python.

Python is now installed.
