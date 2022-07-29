#!/bin/bash

### COMPOSITOR ###

# Picom
picom --experimental-backends &

### KEYBOARD LAYOUT ###

# Latinoamerica
setxkbmap latam &

# Español (España)
# setxkbmap es &

# English (US)
# setxkbmap us &

# English (UK)
# setxkbmap uk &

### SYSTEM STUFF ###

# Screensaver
xscreensaver --no-splash &

# Desktop Manager
lxsession &

### WALLPAPER ###

# Use the default wallpaper
nitrogen --set-zoom-fill --save ~/.config/qtile/wallpaper.jpg &

# Restore the last wallpaper
# nitrogen --restore &

### SYSTRAY ###

# Battery icon
cbatticon &

# Volume icon
volumeicon &

# Udikise (Automount drives)
udiskie -t -N &

# NetworkManager
nm-applet &
