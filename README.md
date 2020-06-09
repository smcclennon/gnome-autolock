# gnome-autolock
Automatically lock your machine immediately after you login/signin after a reboot

Useful for protecting your device from prying eyes when you have "Automatic login" enabled to load your startup applications on boot

The python script will attempt to lock your machine on startup, and retry up to 150 times over the course of 15 seconds before givng up.

## Requirements:
- Python 3
- gnome-screensaver

### Install gnome-screensaver
- Fedora: `sudo dnf install gnome-screensaver`
Test by running `gnome-screensaver-command`

### Install Gnome Autolock
1. Copy [`gnome-autolock.py`](gnome-autolock.py) to `~/Applications`
2. Copy [`gnome-autolock.desktop`](gnome-autolock.desktop) to `~/.local/applications`

`~/` = `/home/user/`
