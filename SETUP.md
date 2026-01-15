# Setup Guide

Quick reference for setting up dotfiles on a new machine.

## Quick Start (Personal Machine)

```bash
git clone https://github.com/madsfors/dotfiles.git ~/.dotfiles
cd ~/.dotfiles
./script/bootstrap
```

## Work Machine Setup

For managed/work machines, run steps individually to stay safe:

```bash
# 1. Clone the repo
git clone https://github.com/madsfors/dotfiles.git ~/.dotfiles
cd ~/.dotfiles

# 2. Install Oh My Zsh and plugins, symlink configs
./script/setup

# 3. Install apps (safe - skips already installed)
brew bundle --file=Brewfile

# 4. Apply macOS preferences (safe - security settings are disabled)
./script/macos-defaults

# 5. Set up Cursor extensions
./script/strap-after-setup
```

### What's safe on work machines

| Safe ✅ | Notes |
|---------|-------|
| `./script/setup` | Just symlinks config files |
| `brew bundle` | Installs apps, skips existing |
| `./script/macos-defaults` | Security settings already disabled |
| `./script/strap-after-setup` | Cursor extensions only |

### What's already disabled for work machines

- FileVault (let IT manage)
- Firewall settings (let IT manage)
- TouchID for sudo (let IT manage)

## Source of Truth

| Config | Location | Sync behavior |
|--------|----------|---------------|
| Shell (zshrc) | `dot/zshrc` | Symlinked — edits sync automatically |
| Git config | `dot/gitconfig` | Symlinked — edits sync automatically |
| Cursor settings | `files/config/cursor/settings.json` | Symlinked — edits sync automatically |
| macOS prefs | `script/macos-defaults` | One-way — update script if you change prefs |
| Apps | `Brewfile` | One-way — update manually if you add/remove apps |

### Updating your dotfiles

For symlinked files (zshrc, gitconfig, Cursor):
```bash
cd ~/.dotfiles
git add -A
git commit -m "Update preferences"
git push
```

For macOS defaults or Brewfile:
1. Change the setting/install the app
2. Update the script/Brewfile to match
3. Commit and push

## Personal-Only Apps

These are commented out in Brewfile (uncomment on personal machines):
- `mullvad-vpn` — VPN for home use
