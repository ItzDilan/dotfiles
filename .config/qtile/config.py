#### QTILE ####

from libqtile.lazy import lazy
from libqtile import bar, layout, widget, qtile
from libqtile.config import Click, Drag, Group, Key, Match, Screen

#### AUTOSTART ####

import os
import subprocess
from libqtile import hook

@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.call([home])

#### VARIABLES ####

alt = "mod1"
mod = "mod4"
terminal = "alacritty"
browser = "firefox"
filemanager = "pcmanfm"
menu = "rofi -show drun"
themechanger = os.path.expanduser('~/.config/qtile/themes/themechanger.py')
qtile_config = os.path.expanduser('~/.config/qtile/config.py')

keys = [

    #### PROGRAMS ####

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
    
    #### HARDWARE ####

    # Volume
    #Key([], "XF86AudioRaiseVolume", lazy.spawn("pamixer --increase 5")),
    #Key([], "XF86AudioLowerVolume", lazy.spawn("pamixer --decrease 5")),
    #Key([], "XF86AudioMute", lazy.spawn("pamixer --toggle-mute")),
    
    # Brightness
    Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set +5%")),
    Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 5%-")),
    
    #### SYSTEM ####

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

    #### WINDOW CONFIGS ####

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

#### COLORS ####

colors = ["#14161b","#727072",
          "#ffffff","#ffffff",
          "#7da4f6","#ffffff",
          "#727072","#ff6188",
          "#7197e7","#a77ac4",
          "#7197e7","#a77ac4",
          "#232f35","#727072"]

#### WORKSPACES ####

# Groups
groups = [Group(i) for i in [
    "NET", "SYS", "DEV", "MSC", "FLS", "MDA", "IMG", "DOC", "GFX",
]]

for i, group in enumerate(groups):
    actual_key = str(i + 1)
    keys.extend([
        Key([mod], actual_key, lazy.group[group.name].toscreen()),
        Key([mod, "shift"], actual_key, lazy.window.togroup(group.name))
    ])

#### LAYOUTS ####

# Layout theme
layout_theme = {"border_width": 2, 
                "margin": 4,
                "border_focus": colors[4],
                "border_normal": colors[0],
                }

# Layouts configs
layouts = [
    layout.Columns(
        **layout_theme,
        border_on_single = True,
        margin_on_single = 4,
        ),
    layout.Max(),
    layout.Floating(
        **layout_theme,
        ),
    ]

# Floating windows
floating_layout = layout.Floating(
    float_rules=[
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),
        Match(wm_class="makebranch"),
        Match(wm_class="maketag"),
        Match(wm_class="ssh-askpass"),
        Match(title="branchdialog"),
        Match(title="pinentry"),
    ],
    border_focus = colors[4],
    border_width = 2,
)

# Drag floating layouts
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]


#### WIDGETS SETTINGS ####

widget_defaults = dict(
    font = "Ubuntu Bold",
    fontsize = 14,
    padding = 2,
)

extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
        widget.GroupBox(
            fontsize = 12,
            active = colors[2],
            inactive = colors[1],
            highlight_method = "block",
            highlight_color = colors[12],
            urgent_alert_method = "block",
            urgent_border = colors[6],
            this_current_screen_border = colors[4],
            this_screen_border = colors[1],
            other_current_screen_border = colors[1],
            other_screen_border = colors[0],
            rounded = False,
            margin_x = 0,
            margin_y = 5,
            padding_y = 15,
            padding_x = 5,
            ),
        widget.Sep(
            padding = 5,
            foreground = colors[0],
            background = colors[0],
            ),
        widget.WindowName(
            fontsize = 12,
            foreground = colors[4],
            max_chars = 55,
            ),
        widget.TextBox(
            "???",
            fontsize = 44,
            font = "UbuntuMono Nerd Font",
            background = colors[0],
            foreground = colors[11],
            padding = -3,
            ),
        widget.TextBox(
            "??? ",
            fontsize = 16,
            font = "UbuntuMono Nerd Font",
            background = colors[11],
            foreground = colors[3],
            ),
        widget.TextBox(
            "ArchLinux ",
            background = colors[11],
            foreground = colors[3],
            mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(terminal + ' -e sudo pacman -Syu')},
            ),
        widget.TextBox(
            "???",
            fontsize = 44,
            font = "UbuntuMono Nerd Font",
            padding = -3,
            background = colors[11],
            foreground = colors[10],
            ),
        widget.TextBox(
            "??? ",
            fontsize = 16,
            font = "UbuntuMono Nerd Font",
            background = colors[10],
            foreground = colors[3],
            ),
        widget.TextBox(
            "Qtile ",
            background = colors[10],
            foreground = colors[3],
            mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(terminal + ' -e nvim ' + qtile_config)},
            ),
        widget.TextBox(
            "???",
            fontsize = 44,
            font = "UbuntuMono Nerd Font",
            foreground = colors[9],
            background = colors[10],
            padding = -3,
            ),
        widget.CurrentLayoutIcon(
            background = colors[9],
            scale = 0.6,
            ),
        widget.CurrentLayout(
            background = colors[9],
            foreground = colors[3],
            ),
        widget.Sep(
            foreground = colors[9],
            background = colors[9],
            padding = 4,
            ),
        widget.TextBox(
            "???",
            fontsize = 44,
            font = "UbuntuMono Nerd Font",
            foreground = colors[8],
            background = colors[9],
            padding = -3,
            ),
        widget.TextBox(
            "??? ",
            fontsize = 16,
            font = "UbuntuMono Nerd Font",
            foreground = colors[3],
            background = colors[8],
            ),
        widget.Clock(
            foreground = colors[3],
            background = colors[8],
            format="%d/%m/%Y - %I:%M %p ",
            ),
        widget.TextBox(
            "???",
            fontsize = 44,
            font = "UbuntuMono Nerd Font",
            foreground = colors[0],
            background = colors[8],
            padding = -3,
            ),
        widget.Systray(
            background = colors[0],
            padding = 6,
            ),
        widget.Sep(
            padding = 6,
            foreground = colors[0],
            background = colors[0],
            ), 
            ],
        31,
        background = colors[0],
        margin = 0,
        opacity = 1.00,
        ),
        ),
        ]

#### IMPORTANT FUNCTIONS ####

dgroups_key_binder = None
dgroups_app_rules = []
follow_mouse_focus = True
bring_front_click = False
cursor_warp = True 
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True
auto_minimize = True
wl_input_rules = None
wmname = "Qtile"
