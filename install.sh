# Instala los programas necesarios
sudo pacman -S xorg xorg-server lightdm lightdm-gtk-greeter qtile alacritty fish starship pcmanfm rofi nitrogen scrot redshift file-roller gvfs glib2 gvfs-mtp udiskie network-manager-applet cbatticon pulseaudio pavucontrol pamixer alsa-utils brightnessctl gedit eog arandr xdg-user-dirs ntfs-3g lxappearance vlc dunst nano neovim lsd bat lxsession xscreensaver volumeicon gnome-themes-extra gtk-engine-murrine --noconfirm

# Genera las carpetas de usuario
xdg-user-dirs-update

# Instala Yay (AUR Helper)
sudo pacman -S git base-devel --noconfirm && git clone https://aur.archlinux.org/yay-git.git && cd yay-git/ && makepkg -si

# Istala fork de Picom (Compositor de ventanas)
yay -S picom-jonaburg-git --noconfirm

# Instala las fuentes necesarias
yay -S nerd-fonts-jetbrains-mono nerd-fonts-ubuntu-mono --noconfirm

# Clona mi repositorio y usa mis configuraciones
git clone https://github.com/itzdilan/dotfiles.git && cp -r dotfiles/.config ~/ && cp -r dotfiles/.local ~/

# Cambiar la shell por defecto
sudo usermod --shell /usr/bin/fish $USER
sudo usermod --shell /usr/bin/fish root

# Instala tema de LightDM
sudo pacman -S lightdm-webkit2-greeter --noconfirm && yay -S lightdm-webkit-theme-aether --noconfirm

# Instala tema de NeoVim
git clone https://github.com/NvChad/NvChad ~/.config/nvim --depth 1 && nvim +'hi NormalFloat guibg=#1e222a' +PackerSync
