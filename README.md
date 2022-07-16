# Qtile

![ArchLinux](https://user-images.githubusercontent.com/99371498/179362202-5008d2ea-f15a-4223-bbcd-b4183059f362.png)

# Índice 
- [Instalación de Qtile](#instalación-de-qtile)
- [Genera las carpetas de usuario](#genera-las-carpetas-de-usuario)
- [Instala un Aur Helper](#instala-un-aur-helper)
- [Compositor de ventanas](#compositor-de-ventanas)
- [Fuente necesaria](#fuente-necesaria)
- [Utiliza mis configuraciones](#utiliza-mis-configuraciones)
- [Cambia la Shell por defecto](#cambia-la-shell-por-defecto)
- [Temas](#temas)

# Instalación de Qtile y Programas necesarios

Programas que utilizo:

```bash
sudo pacman -S xorg xorg-server lightdm lightdm-gtk-greeter qtile alacritty fish starship pcmanfm rofi nitrogen scrot redshift file-roller gvfs glib2 gvfs-mtp udiskie network-manager-applet cbatticon pulseaudio pavucontrol pamixer alsa-utils brightnessctl gedit eog arandr xdg-user-dirs ntfs-3g lxappearance vlc dunst nano neovim lsd bat lxsession xscreensaver
```

# Genera las carpetas de usuario

Con el siguiente comando se generarán las carpetas comúnes de usuario: Descargas, Imágenes, Documentos...

```bash
xdg-user-dirs-update
```

# Instala un Aur helper

Programas necesarios:

```bash
sudo pacman -S git base-devel
```

Clona el repositorio de Yay o Paru

En Arch Linux y sus derivadas, podemos utilizar un "Aur Helper", para facilitar la instalación de paquetes "AUR". Aquí te dejo 2 "Aur Helpers", puedes utilizar uno o ambos:

Yay:

```bash
git clone https://aur.archlinux.org/yay-git.git
cd yay-git/ 
makepkg -si
```

Paru:

```bash
git clone https://aur.archlinux.org/paru-git.git
cd paru-git/ 
makepkg -si
````
# Compositor de ventanas

Yay:

```bash
yay -S picom-jonaburg-git
```

Paru:

```bash
paru -S picom-jonaburg-git
```

# Fuente necesaria


Yay:

```bash
yay -S nerd-fonts-ubuntu-mono
```

Paru:

```bash
paru -S nerd-fonts-ubuntu-mono
```

Debes reiniciar la sesión para que el sistema cargue las fuentes:

# Clona mi repositorio


```bash
git clone https://github.com/itzdilan/dotfiles.git
```


Mueve las carpetas a sus lugares:

```bash
cp -r dotfiles/.config ~/
cp -r dotfiles/.local ~/
cp dotfiles/.xprofile ~/
```

# Cambia la Shell por defecto

En mi caso, utilizo fish como shell por defecto:

```bash
sudo usermod --shell /usr/bin/fish user
sudo usermod --shell /usr/bin/fish root
```

# Temas

--- Fondo de pantalla ---

Podrás encontrar algunos fondos de pantalla en "~/.config/qtile/Wallpapers/". Puedes cambiarlos utilizando Nitrogen.

--- Tema de LightDM: ---

```bash
sudo pacman -S lightdm-webkit2-greeter
```

Paru:

```bash
paru -S lightdm-webkit-theme-aether
```

Yay:

```bash
yay -S lightdm-webkit-theme-aether
```

Pudes cambiar la configuración desde el siguiente archivo:

```bash
sudo nano /etc/lightdm/lightdm-webkit2-greeter.conf
```

En mi caso, he cambiado el tema por "antergos", puedes hacerlo modificando la línea de "webkit_theme":

```bash
webkit_theme = antergos
```

--- Tema de NeoVim ---

Si prefieres utilizar NeoVim, aquí tienes el tema que utilizo de este:

```bash
cd
git clone https://github.com/NvChad/NvChad ~/.config/nvim --depth 1
nvim +'hi NormalFloat guibg=#1e222a' +PackerSync
```

Selecciona el tema "Gruvbox" presionando la tecla Espacio + th en NeoVim.


--- Tema de GRUB: ---

Descarga el tema "Vimix" para GRUB:

https://www.gnome-look.org/p/1009236/

Suponiendo que estás en la carpeta donde se encuentra el tema de GRUB, ejecuta los siguientes comandos:

Puedes cambiar "Vimix-1080p.tar.xz" por las variantes que hay (Vimix-4k.tar.xz) | (Vimix-2k.tar.xz).

```bash
tar xvf Vimix-1080p.tar.xz
cd Vimix-1080p
sudo bash install.sh
```

--- Tema GTK ---

https://www.gnome-look.org/p/1681313/

--- Tema de Íconos ---

https://www.gnome-look.org/p/1681460/
