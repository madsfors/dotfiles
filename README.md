# Mads' Dotfiles

> 👢 Bootstrap your macOS system with a personalized setup

This repository contains my complete macOS environment setup, built on top of the excellent [Strap](https://github.com/MikeMcQuaid/strap) by Mike McQuaid.

## Features

- **Automated Setup**: One-command bootstrap for new Macs
- **Comprehensive**: Installs apps, configures system preferences, and sets up tools
- **Idempotent**: Safe to run multiple times
- **Personalized**: Tailored specifically for my workflow

## Quick Start

```bash
# Clone the repository to ~/.dotfiles
git clone https://github.com/madsfors/dotfiles.git ~/.dotfiles
cd ~/.dotfiles

# Run the bootstrap script
./script/bootstrap
```

## What It Does

### 🍺 Applications & Tools (via Homebrew)

- **Design**: Figma, Nucleo, ImageOptim
- **Productivity**: Raycast, Things 3, Bartender, Obsidian
- **Development**: Cursor, GitHub Desktop
- **Browsers**: Arc
- **Media**: Spotify, IINA, OBS, Calibre
- **Utilities**: CleanShot, Hazel, MeetingBar, Flux
- **Communication**: Microsoft Office suite

### ⚙️ System Configuration

- Dark mode enabled
- Fast key repeat rates
- Dock autohide with custom animations
- Hot corners configured
- Trackpad and input optimizations
- Finder preferences (show hidden files, list view, etc.)

### 🔧 Environment

- **Shell**: Zsh with Oh My Zsh (robbyrussell theme)
- **Git**: Configured with aliases and sensible defaults
- **Node.js**: Latest version with npm
- **Editor**: Cursor with Cursor Dark theme, iA Writer Mono font, and essential extensions
- **Visual Consistency**: Dark mode system-wide

## File Structure

```
~/.dotfiles/
├── Brewfile                 # Homebrew packages and applications
├── README.md               # This file
├── dot/                    # Dotfiles (symlinked to ~/)
│   ├── gitconfig          # Git configuration
│   ├── gitignore_global   # Global gitignore
│   ├── zshrc              # Zsh configuration
│   └── zsh_functions      # Custom shell functions
├── files/                 # Configuration files
│   └── config/
│       └── cursor/        # Cursor editor settings
└── script/                # Setup and utility scripts
    ├── bootstrap          # Main bootstrap script
    ├── macos-defaults     # macOS system preferences
    ├── setup              # Dotfiles symlink setup
    └── strap-after-setup  # Post-bootstrap configuration
```

## Individual Scripts

You can run individual components if needed:

```bash
# Just install applications
brew bundle --file=Brewfile

# Just configure macOS defaults
./script/macos-defaults

# Just setup dotfiles
./script/setup

# Just run final configuration
./script/strap-after-setup
```

## Customization

This setup is highly personalized for my workflow. To adapt it for yourself:

1. **Fork this repository**
2. **Update personal information**:
   - `dot/gitconfig`: Change name and email
   - `script/strap-after-setup`: Update SSH key email
   - `Brewfile`: Add/remove applications as needed
3. **Modify configurations**:
   - `dot/zshrc`: Adjust aliases and functions
   - `script/macos-defaults`: Change system preferences
   - `files/config/cursor/`: Customize editor settings

## Manual Steps

After running the bootstrap, you may want to:

- Add your SSH key to GitHub (will be displayed after setup)
- Sign in to all applications
- Configure 1Password browser integration
- Set up any remaining app-specific preferences
- Optional: Install [Dank Mono](https://philpl.gumroad.com/l/dank-mono) font (paid)

## Inspiration

This setup is built on top of and inspired by:

- [Strap](https://github.com/MikeMcQuaid/strap) by Mike McQuaid
- [Mathias Bynens' dotfiles](https://github.com/mathiasbynens/dotfiles)
- [Holman's dotfiles](https://github.com/holman/dotfiles)

## License

This project is licensed under the MIT License - see the LICENSE file for details.

---

Made with ❤️ by [Mads Fors](https://github.com/madsfors)
