# Qtile

# Temas disponibles

<details><summary> <b>Imágenes (Click para expandir)</b></summary>

Gruvbox

![ArchLinux](https://user-images.githubusercontent.com/99371498/179362202-5008d2ea-f15a-4223-bbcd-b4183059f362.png)

Dracula

![Dracula](https://user-images.githubusercontent.com/99371498/179366453-41202544-c815-4665-9032-7c1a65f8d991.png)

MonokaiPro

![Monokai](https://user-images.githubusercontent.com/99371498/179366458-152a9c54-b1cd-4290-9658-5461e7590a8c.png)

Material Ocean

![MaterialOcean](https://user-images.githubusercontent.com/99371498/179366463-b1bef5d9-9b33-4162-8c49-ee2c629c1425.png)

Solarized Dark

![SolarizedDark](https://user-images.githubusercontent.com/99371498/179366467-0ad962cb-d4b7-4bb0-b16d-2fe21b036130.png)

Nord

![Nord](https://user-images.githubusercontent.com/99371498/179366472-de2425b5-2755-4b4e-a10f-eca8e6b80f48.png)

</details>


# Índice 
- [Imports](#imports)
- [Autostart](#autostart)
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
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.call([home])
```

# Temas

--- Tema de GRUB: ---

https://www.gnome-look.org/p/1009236/

--- Tema GTK ---

https://www.gnome-look.org/p/1681313/

--- Tema de Íconos ---

https://www.gnome-look.org/p/1681460/
