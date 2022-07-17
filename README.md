# Gruvbox Dark

![ArchLinux](https://user-images.githubusercontent.com/99371498/179362202-5008d2ea-f15a-4223-bbcd-b4183059f362.png)

# Dracula

![Dracula](https://user-images.githubusercontent.com/99371498/179366453-41202544-c815-4665-9032-7c1a65f8d991.png)

# Monokai Pro

![Monokai](https://user-images.githubusercontent.com/99371498/179366458-152a9c54-b1cd-4290-9658-5461e7590a8c.png)

# Material Ocean

![MaterialOcean](https://user-images.githubusercontent.com/99371498/179366463-b1bef5d9-9b33-4162-8c49-ee2c629c1425.png)

# Solarized Dark

![SolarizedDark](https://user-images.githubusercontent.com/99371498/179366467-0ad962cb-d4b7-4bb0-b16d-2fe21b036130.png)

# Nord

![Nord](https://user-images.githubusercontent.com/99371498/179366472-de2425b5-2755-4b4e-a10f-eca8e6b80f48.png)



# Índice 
- [Imports](#imports)
- [Autostart](#autostart)
- [Variables](#variables)
- [Keys](#keys)
- [Groups](#groups)
- [Temas](#temas)

# Imports

```bash
from libqtile.lazy import lazy
from themes.colors import colors
from libqtile import bar, layout, widget, qtile
from libqtile.config import Click, Drag, Group, Key, Match, Screen
```

# Autostart

```bash
import os
import subprocess
from libqtile import hook

@hook.subscribe.startup_once
def autostart():
    autostart_sh = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.call([autostart_sh])
```

# Variables

```bash
alt = "mod1"
mod = "mod4"
terminal = "alacritty"
browser = "chromium"
filemanager = "pcmanfm"
menu = "rofi -show drun"
themechanger = os.path.expanduser('~/.config/qtile/themes/themechanger.py')
qtile_config = os.path.expanduser('~/.config/qtile/config.py')
```

# Keys

```bash
keys = [

    ### PROGRAMS ###

    # Terminal
    Key([mod], "Return", lazy.spawn(terminal)),

    # Browser
    Key([mod], "b", lazy.spawn(browser)),

    # Menu
    Key([mod], "m", lazy.spawn(menu)),

    # File Manager
    Key([mod], "e", lazy.spawn(filemanager)),

    # Nitrogen
    Key([mod], "n", lazy.spawn("nitrogen")),
    Key([mod, "shift"], "n", lazy.spawn("nitrogen --set-zoom-fill --random --save")),

    # Redshit
    Key([mod], "r", lazy.spawn("redshift -O 4000")),
    Key([mod, "shift"], "r", lazy.spawn("redshift -x")),

    # Screenshot
    Key([mod], "s", lazy.spawn("scrot")),
    Key([mod, "shift"], "s", lazy.spawn("scrot -x")),

    # Theme changer
    Key([mod], "t", lazy.spawn(terminal + ' -e python3 ' + themechanger)),
    
     ### HARDWARE ###

    # Volume
    Key([], "XF86AudioRaiseVolume", lazy.spawn("pamixer --increase 5")),
    Key([], "XF86AudioLowerVolume", lazy.spawn("pamixer --decrease 5")),
    Key([], "XF86AudioMute", lazy.spawn("pamixer --toggle-mute")),
    
    # Brightness
    Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set +5%")),
    Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 5%-")),
    
    ### SYSTEM ###

    # Shutdown
    Key([mod, "control"], "a", lazy.spawn("poweroff")),

    # Reboot
    Key([mod, "control"], "z", lazy.spawn("reboot")),

    # Exit from Qtile
    Key([mod, "control"], "q", lazy.shutdown()),

    # Suspend
    Key([mod, "control"], "w", lazy.spawn("xscreensaver-command -suspend")),

    # Reload
    Key([mod, "control"], "r", lazy.restart()),

    ### WINDOW CONFIGS ###

    # Switch between windows
    Key([mod], "h", lazy.layout.left()),
    Key([mod], "l", lazy.layout.right()),
    Key([mod], "j", lazy.layout.down()),
    Key([mod], "k", lazy.layout.up()),

    # Move windows between left/right columns
    Key([mod, "shift"], "h", lazy.layout.shuffle_left()),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right()),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down()),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up()),

    # Grow windows
    Key([mod, "control"], "h", lazy.layout.grow_left()),
    Key([mod, "control"], "l", lazy.layout.grow_right()),
    Key([mod, "control"], "j", lazy.layout.grow_down()),
    Key([mod, "control"], "k", lazy.layout.grow_up()),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout()),
    Key([mod], "q", lazy.window.kill()),
]
```

# Groups

```bash
groups = [Group(i) for i in [
    "NET", "SYS", "DEV", "MSC", "FLS", "MDA", "IMG", "DOC", "GFX",
]]

for i, group in enumerate(groups):
    actual_key = str(i + 1)
    keys.extend([
        Key([mod], actual_key, lazy.group[group.name].toscreen()),
        Key([mod, "shift"], actual_key, lazy.window.togroup(group.name))
    ])
```

# Temas

--- Tema de GRUB: ---

https://www.gnome-look.org/p/1009236/

--- Tema GTK ---

https://www.gnome-look.org/p/1681313/

--- Tema de Íconos ---

https://www.gnome-look.org/p/1681460/
