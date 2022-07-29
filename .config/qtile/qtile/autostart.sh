#!/bin/bash

### COMPOSITOR ###

# Picom
#picom --experimental-backends &

### KEYBOARD LAYOUT ###

# Latinoamerica
setxkbmap latam &

# English (US)
# setxkbmap us &

# English (UK)
# setxkbmap uk &

### SYSTEM STUFF ###

# Screensaver
xscreensaver --no-splash &

# Desktop Manager
lxsession &

# Wallpaper
#nitrogen --restore &

### SYSTRAY ###

# Battery icon
cbatticon &

# Volume icon
volumeicon &

# Udikise (Automount disks)
udiskie -t -N &

# NetworkManager
nm-applet &
