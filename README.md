# Mads' Dotfiles

> 👢 Bootstrap your macOS development system with a personalized setup

This repository contains my complete macOS development environment setup, built on top of the excellent [Strap](https://github.com/MikeMcQuaid/strap) by Mike McQuaid.

## Features

- **Automated Setup**: One-command bootstrap for new Macs
- **Comprehensive**: Installs apps, configures system preferences, and sets up development tools
- **Idempotent**: Safe to run multiple times
- **Personalized**: Tailored specifically for my development workflow

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

- **Development**: Cursor, GitHub Desktop, Figma
- **Productivity**: Notion, Raycast (with window management), Things 3, Bartender
- **Communication**: Microsoft Teams (pre-installed)
- **Browsers**: Arc
- **Media**: Spotify, IINA, OBS
- **Utilities**: Karabiner-Elements, CleanShot, Hazel
- **And many more...**

### ⚙️ System Configuration

- Dark mode enabled
- Fast key repeat rates
- Dock autohide with custom animations
- Hot corners configured
- Security settings (FileVault, Firewall)
- Trackpad and input optimizations

### 🔧 Development Environment

- **Shell**: Zsh with Oh My Zsh (robbyrussell theme)
- **Git**: Configured with aliases and sensible defaults
- **Node.js**: Latest version with npm and pnpm
- **Package Managers**: Homebrew, npm, pnpm pre-configured
- **Editor**: Cursor with Night Owl theme, Dank Mono font, and curated extensions
- **Visual Consistency**: Dark mode system-wide with matching terminal/editor themes

### ⌨️ Keyboard Customization

- **Karabiner-Elements**: Caps Lock → Hyper Key (⌃⌥⇧⌘) + Escape
- Custom key mappings for enhanced productivity

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
│       └── karabiner/     # Karabiner-Elements config
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
   - `files/config/karabiner/`: Customize keyboard mappings

## Manual Steps

After running the bootstrap, you may want to:

- Add your SSH key to GitHub (will be displayed after setup)
- Install premium fonts: [Dank Mono](https://philpl.gumroad.com/l/dank-mono), [Departure Mono](https://departuremono.com/) (paid fonts, free alternatives included)
- Sign in to all applications
- Configure 1Password browser integration
- Set up any remaining app-specific preferences
- Configure cloud sync for applications that support it

## Inspiration

This setup is built on top of and inspired by:

- [Strap](https://github.com/MikeMcQuaid/strap) by Mike McQuaid
- [Mathias Bynens' dotfiles](https://github.com/mathiasbynens/dotfiles)
- [Holman's dotfiles](https://github.com/holman/dotfiles)

## License

This project is licensed under the MIT License - see the LICENSE file for details.

---

Made with ❤️ by [Mads Fors](https://github.com/madsfors)
