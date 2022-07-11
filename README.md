# Qtile

![Nighttime](https://user-images.githubusercontent.com/99371498/178377950-95031d55-2478-47c1-82a3-f2fcfc883c05.png)

# Índice 
- [Instalación de Qtile](#instalación-de-qtile)
- [Genera las carpetas de usuario](#genera-las-carpetas-de-usuario)
- [Instala un Aur Helper](#instala-un-aur-helper)
- [Fuente necesaria](#fuente-necesaria)
- [Utiliza mis configuraciones](#utiliza-mis-configuraciones)
- [Cambia la Shell por defecto](#cambia-la-shell-por-defecto)
- [Temas](#temas)

# Instalación de Qtile y Programas necesarios

Programas que utilizo:

```bash
sudo pacman -S xorg xorg-server lightdm lightdm-gtk-greeter qtile alacritty fish pcmanfm rofi nitrogen scrot redshift file-roller gvfs glib2 gvfs-mtp udiskie network-manager-applet cbatticon pulseaudio pavucontrol pamixer alsa-utils brightnessctl playerctl gedit eog arandr picom xdg-user-dirs ntfs-3g lxappearance vlc dunst nano neovim lsd bat
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

Clona el repositorio de Yay/Paru

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

# Fuente necesaria

Si no instalamos esta fuente, las letras y widgets de mi configuración, no se podrán ver correctamente:

Yay:

```bash
yay -S nerd-fonts-ubuntu-mono
```

Paru:

```bash
paru -S nerd-fonts-ubuntu-mono
```

Debes reiniciar la sesión para que el sistema cargue las fuentes:

# Utiliza mis configuraciones

Clona mi repositorio:

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

Utilizando el programa "Nitrogen", podrás cambiar los fondos de pantalla que utilices.

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

--- Tema de Fish shell ---

```bash
sudo pacman -S fisher
fisher install IlanCosman/tide@v5
```

--- Tema de NeoVim ---

Si prefieres utilizar NeoVim, aquí tienes el tema que utilizo de este:

```bash
cd
git clone https://github.com/NvChad/NvChad ~/.config/nvim --depth 1
nvim +'hi NormalFloat guibg=#1e222a' +PackerSync
```

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
