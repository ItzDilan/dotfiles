### QTILE ###

from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

mod = "mod4"
terminal = "alacritty"
browser = "chromium"
filemanager = "pcmanfm"
menu = "rofi -show drun"

keys = [
    ### PROGRAMS ###

    # Terminal
    Key([mod], "Return", lazy.spawn(terminal)),

    # Browser
    Key([mod], "b", lazy.spawn(browser)),

    # Menu
    Key([mod], "m", lazy.spawn(menu)),

    # GIMP
    Key([mod], "g", lazy.spawn("gimp")),

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

    ### HARDWARE ###

    # Volume
    Key([], "XF86AudioRaiseVolume", lazy.spawn("pamixer --increase 5")),
    Key([], "XF86AudioLowerVolume", lazy.spawn("pamixer --decrease 5")),
    Key([], "XF86AudioMute", lazy.spawn("pamixer --toggle-mute")),
    
    # Brightness
    Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set +5%")),
    Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 5%-")),

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
    Key([mod, "control"], "r", lazy.reload_config()),
    Key([mod, "control"], "q", lazy.shutdown()),
]

### COLORS ###

colors = ["#151515","#404040",
          "#e9e9e9","#000000",
          "#3f5965","#ffffff",
          "#727072","#ff6188",
          "#8fa1b3","#a3be8c",
          "#b48ead","#bf616a",
          "#232f35","#414753"]

### WORKSPACES ###

groups = [Group(i) for i in [
    "NET", "SYS", "DEV", "MSC", "FLS", "MDA", "IMG", "DOC", "GFX",
]]

for i, group in enumerate(groups):
    actual_key = str(i + 1)
    keys.extend([
        Key([mod], actual_key, lazy.group[group.name].toscreen()),
        Key([mod, "shift"], actual_key, lazy.window.togroup(group.name))
    ])

# Layout theme
layout_theme = {"border_width": 2, 
                "margin": 4,
                "border_focus": colors[4],
                "border_normal": colors[0],
                }

# Layouts config
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

widget_defaults = dict(
    font = "UbuntuMono Nerd Font Bold",
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
            font = "Ubuntu Bold",
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
            font = "Liberation Sans Bold",
            fontsize = 12,
            foreground = colors[8],
            max_chars = 70,
            ),
        widget.TextBox(
            "",
            fontsize = 44,
            foreground = colors[13],
            background = colors[0],
            padding = -3,
            ),
        widget.Systray(
            background = colors[13],
            padding = 4,
            ),
        widget.Sep(
            padding = 4,
            foreground = colors[13],
            background = colors[13],
            ),
        widget.TextBox(
            "",
            fontsize = 44,
            background = colors[13],
            foreground = colors[11],
            padding = -3,
            ),
        widget.TextBox(
            " ",
            fontsize = 16,
            background = colors[11],
            foreground = colors[3],
            ),
        widget.TextBox(
            "ArchLinux ",
            background = colors[11],
            foreground = colors[3],
            mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(myTerm + ' -e sudo pacman -Syu')},
            ),
        widget.TextBox(
            "",
            fontsize = 44,
            padding = -3,
            background = colors[11],
            foreground = colors[10],
            ),
        widget.TextBox(
            " ",
            fontsize = 16,
            background = colors[10],
            foreground = colors[3],
            ),
        widget.TextBox(
            "Qtile ",
            background = colors[10],
            foreground = colors[3],
            mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(myTerm + ' -e nvim /home/dilan/.config/qtile/settings/keys.py')},
            ),
        widget.TextBox(
            "",
            fontsize = 44,
            foreground = colors[9],
            background = colors[10],
            padding = -3,
            ),
       widget.CurrentLayoutIcon(
            background = colors[9],
            scale = 0.60,
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
            "",
            fontsize = 44,
            foreground = colors[8],
            background = colors[9],
            padding = -3,
            ),
        widget.Clock(
            foreground = colors[3],
            background = colors[8],
            format="  %d/%m/%Y   %I:%M %p ",
            ),
            ],
        31,
        background = colors[0],
        margin = 0,
        opacity = 0.90,
        ),
        ),
        ]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = True 
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True
auto_minimize = True
wl_input_rules = None
wmname = "Qtile"
