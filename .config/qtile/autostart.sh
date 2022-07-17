#!/bin/bash

# Compositor
picom --experimental-backends &

### Keyboard Layout ###

# Latinoamerica
setxkbmap latam &

# English (US)
# setxkbmap us &

# English (UK)
# setxkbmap uk &

# Wallpaper
nitrogen --restore &

# Battery icon
cbatticon &

# Volume icon
volumeicon &

# Udikise (Automount disks)
udiskie -t -N &

# NetworkManager
nm-applet &

# Screensaver
xscreensaver --no-splash &

# Desktop Manager
lxsession &
