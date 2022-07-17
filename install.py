# Imports
import os
import sys
import time

# Limpiar la pantalla
def clean():
    os.system("clear")
clean()

# time.sleep
def wait():
    time.sleep(0.5)

# Espaciador
def spacer():
    print("")

# Cargando
def loading():
    clean()
    spacer()
    print(" Cargando.")
    wait()
    clean()
    spacer()
    print(" Cargando..")
    wait()
    clean()
    spacer()
    print(" Cargando...")
    wait()
    clean()
    spacer()
    print(" Cargando.")
    wait()
    clean()
    spacer()
    print(" Cargando..")
    wait()
    clean()
    spacer()
    print(" Cargando...")
    wait()
    clean()

# ¡Completado!
def done():
    clean()
    spacer()
    print(" ¡Completado!")
    wait()
    clean()

# Saliendo...
def exiting():
    clean()
    spacer()
    print(" Saliendo.")
    wait()
    clean()
    spacer()
    print(" Saliendo..")
    wait()
    clean()
    spacer()
    print(" Saliendo...")
    wait()
    clean()
    sys.exit()

# Omitiendo...
def skip():
    clean()
    spacer()
    print(" Omitiendo.")
    wait()
    spacer()
    print(" Omitiendo..")
    wait()
    spacer()
    print(" Omitiendo...")
    wait()
    clean()

# Atajos de teclado
def keybindings():
    print(" ------------ Programas ------------")
    print(" Win + T = Cambiador de temas")
    print(" Win + Enter = Terminal")
    print(" Win + B = Navegador Web")
    print(" Win + M = Menú Rofi")
    print(" Win + E = Explorador de archivos")
    print(" Win + N = Nitrogen [Fondos de pantalla]")
    print(" Win + Shift + N = Fondo de pantallla aleatorio")
    print(" Win + R = Activa luz nocturna [Redshift]")
    print(" Win + Shift + R = Desactiva luz nocturna")
    print(" Win + S = Tomar captura de pantalla completa")
    print(" Win + Shift + S = Tomar captura recortada")
    spacer()
    print(" ------------ Sistema ------------")
    print(" Win + Control + A = Apagar el equipo")
    print(" Win + Control + Z = Reiniciar el equipo")
    print(" Win + Control + Q = Cerrar sesión")
    print(" Win + Control + W = Suspender")
    print(" Win + Control + R = Recargar Qtile")
    spacer()
    print(" ------------ Configuración de ventanas ------------")
    spacer()
    print(" --- Cambiar entre ventanas ---")
    print(" Win + H = Ventana de la izquierda")
    print(" Win + L = Ventana de la derecha")
    print(" Win + J = Ventana de abajo")
    print(" Win + K = Ventana de arriba")
    print("")
    print(" --- Mover ventanas ---")
    print(" Win + Shift + H = Hacia la izquierda")
    print(" Win + Shift + L = Hacia la derecha")
    print(" Win + Shift + J = Hacia arriba")
    print(" Win + Shift + K = Hacia abajo")
    print("")
    print(" --- Aumentar tamaño de ventanas ---")
    print(" Win + Control + H = Aumentar hacia la izquierda")
    print(" Win + Control + L = Aumentar hacia la derecha")
    print(" Win + Control + J = Aumentar hacia abajo")
    print(" Win + Control + K = Aumentar hacia arriba")

# Bienvenida
def welcome():
    clean()
    spacer()
    print(" Bienvenido a mi script de instalación.")
    print(" Con este script podrás configurar el sistema a tu gusto y utilizar mis configuraciones.")
    spacer()
    print(" ¿Quieres continuar?")
    print(" 1. Sí")
    print(" 2. No")
    spacer()
    run_or_not = int(input(" --> "))
    if run_or_not == 1:
        loading()
        done()
    else:
        exiting()

# Despedida
def byebye():
    clean()
    spacer()
    print(" ¡Has completado la configuración!")
    wait()
    print(" Aquí te dejo una lista con los atajos de teclado")
    spacer()
    keybindings()

# Clonando repositorio...
def clone():
    clean()
    spacer()
    print(" Clonando repositorio.")
    wait()
    clean()
    spacer()
    print(" Clonando repositorio..")
    wait()
    clean()
    spacer()
    print(" Clonando repositorio...")
    wait()
    clean()
    os.system(" git clone https://github.com/itzdilan/dotfiles.git && cp -r dotfiles/.config ~/ && cp -r dotfiles/.local ~/")
    clean()

# Bienvenida
welcome()

# Lista de paquetes
lista_paquetes_1 = " xorg xorg-server lightdm lightdm-gtk-greeter qtile alacritty fish starship pcmanfm rofi nitrogen scrot redshift file-roller gvfs glib2 gvfs-mtp udiskie network-manager-applet cbatticon pulseaudio pavucontrol pamixer alsa-utils brightnessctl gedit eog arandr xdg-user-dirs ntfs-3g lxappearance vlc dunst nano neovim lsd bat lxsession xscreensaver volumeicon gnome-themes-extra gtk-engine-murrine python-colorama"
spacer()
print(" ¿Instalar los siguientes paquetes?")
spacer()
print(lista_paquetes_1)
print(" 1. Sí")
print(" 2. No")
spacer()

# Respuesta de paquetes #1
r1 = int(input(" --> "))

if r1 == 1:
    os.system("sudo pacman -S --noconfirm " + lista_paquetes_1)
    # Generar carpetas de usuario
    os.system("xdg-user-dirs-update")
    done()
elif r1 == 2:
    exiting()
    
# Instalación de AUR Helper
spacer()
print(" ¿Cuál 'AUR Helper' prefieres?")
print(" 1. Yay")
print(" 2. Paru")
spacer()

# Respuesta de paquetes #2
r2 = int(input("--> "))

if r2 == 1:
    spacer()
    os.system("sudo pacman -S git base-devel --noconfirm && git clone https://aur.archlinux.org/yay-git.git && cd yay-git/ && makepkg -si")
    done()

elif r2 == 2:
    spacer()
    os.system("sudo pacman -S git base-devel --noconfirm && git clone https://aur.archlinux.org/paru-git.git && cd paru-git/ && makepkg -si")
    done()
print(" ¿Cuál AUR Helper has elegido?")
print(" 1. Yay")
print(" 2. Paru")
spacer()

# AUR Helper
aur_helper = int(input("--> "))
clean()

# Instala fork de Picom (Compositor de ventanas)
spacer()
print(" ¿Quiéres instalar el compositor de ventanas Picom-Jonaburg?")
print(" 1. Sí")
print(" 2. No")
spacer()

# Respuesta de paquetes #3
r3 = int(input(" --> "))

if r3 == 1:
    spacer()
    if aur_helper == 1:
        os.system("yay -S picom-jonaburg-git --noconfirm")
    elif aur_helper == 2:
        os.system("paru -S picom-jonaburg-git --noconfirm")
elif r3 == 2:
    skip()

# Instalación de las fuentes necesarias

# Lista de fuentes
lista_fuentes = " nerd-fonts-jetbrains-mono nerd-fonts-ubuntu-mono"

print(" Las siguientes fuentes son necearias: " + lista_fuentes)
print(" 1. Instalar")
print(" 2. No instalar (No recomendado)")
spacer()

# Respuesta de paquetes #4
r4 = int(input(" --> "))

if r4 == 1:
    spacer()
    if aur_helper == 1:
        os.system("yay -S nerd-fonts-jetbrains-mono nerd-fonts-ubuntu-mono --noconfirm")
    elif aur_helper == 2:
        os.system("paru -S nerd-fonts-jetbrains-mono nerd-fonts-ubuntu-mono --noconfirm")
    done()
elif r4 == 2:
    skip()

# Clonar mi repositorio
clone()

# Cambiar la shell
print(" ¿Quieres utilizar Fish como Shell?")
print(" 1. Sí")
print(" 2. No")
spacer()

# Repuesta de paquetes #5
r5 = int(input(" --> "))

if r5 == 1:
    spacer()
    os.system("sudo usermod --shell /usr/bin/fish $USER")
    os.system("sudo usermod --shell /usr/bin/fish root")
    done()
if r5 == 2:
    skip()

# Instala tema de LightDM
print(" ¿Quieres instalar un tema personalizado de LightDM?")
print(" 1. Sí")
print(" 2. No")
spacer()

# Respuseta de paquetes #6
r6 = int(input(" --> "))

if r6 == 1:
    spacer()
    os.system("sudo pacman -S lightdm-webkit2-greeter --noconfirm")
    if aur_helper == 1:
        os.system("yay -S lightdm-webkit-theme-aether --noconfirm")
    elif aur_helper == 2:
        os.system("paru -S lightdm-webkit-theme-aether --noconfirm")
    done()
elif r6 == 2:
    skip()

# Instala tema de NeoVim
print(" ¿Quieres instalar un tema personalizado de NeoVim?")
print(" 1. Sí")
print(" 2. No")
spacer()

# Respuesta de paquetes #7
r7 = int(input(" --> "))

if r7 == 1:
    spacer()
    os.system("cd && git clone https://github.com/NvChad/NvChad ~/.config/nvim --depth 1 && nvim +'hi NormalFloat guibg=#1e222a' +PackerSync")
    done()
elif r7 == 2:
    skip()
