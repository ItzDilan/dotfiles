### QTILE THEME CHANGER ###

from colorama import init, Fore
import os

def menu():
    print(Fore.WHITE + "------------------")
    print(Fore.MAGENTA + "1. Dracula")
    print(Fore.YELLOW + "2. Gruvbox Dark")
    print(Fore.WHITE + "3. Nord")
    print(Fore.BLUE + "4. Solarized Dark")
    print(Fore.GREEN + "5. Monokai Pro")
    print(Fore.RED + "6. Material Ocean")
    print(Fore.LIGHTCYAN_EX + "7. TomorrowNight")
    print(Fore.LIGHTBLUE_EX + "8. Rxyhn")
    print(Fore.WHITE + "------------------")

menu()

theme = int(input("--> "))

# Dracula
if theme == 1:
    os.system("cp ~/.config/qtile/themes/Dracula/colors.py ~/.config/qtile/themes")
    os.system("cp ~/.config/alacritty/themes/Dracula/alacritty.yml ~/.config/alacritty")
    os.system("cp ~/.local/share/rofi/themes/Dracula/onedark.rasi ~/.local/share/rofi/themes")
    os.system("cp ~/.config/dunst/themes/Dracula/dunstrc ~/.config/dunst")
    os.system("qtile cmd-obj -o cmd -f restart")
    os.system("nitrogen --set-zoom-fill --save --random ~/.config/qtile/themes/Dracula/")
    os.system("killall dunst'")

# Gruvbox Dark
elif theme == 2:
    os.system("cp ~/.config/qtile/themes/GruvboxDark/colors.py ~/.config/qtile/themes")
    os.system("cp ~/.config/alacritty/themes/GruvboxDark/alacritty.yml ~/.config/alacritty")
    os.system("cp ~/.local/share/rofi/themes/GruvboxDark/onedark.rasi ~/.local/share/rofi/themes")
    os.system("cp ~/.config/dunst/themes/GruvboxDark/dunstrc ~/.config/dunst")
    os.system("qtile cmd-obj -o cmd -f restart")
    os.system("nitrogen --set-zoom-fill --save --random ~/.config/qtile/themes/GruvboxDark/")
    os.system("killall dunst'")

# Nord
elif theme == 3:
    os.system("cp ~/.config/qtile/themes/Nord/colors.py ~/.config/qtile/themes")
    os.system("cp ~/.config/alacritty/themes/Nord/alacritty.yml ~/.config/alacritty")
    os.system("cp ~/.local/share/rofi/themes/Nord/onedark.rasi ~/.local/share/rofi/themes")
    os.system("cp ~/.config/dunst/themes/Nord/dunstrc ~/.config/dunst")
    os.system("qtile cmd-obj -o cmd -f restart")
    os.system("nitrogen --set-zoom-fill --save --random ~/.config/qtile/themes/Nord/")
    os.system("killall dunst")

# Solarized Dark
elif theme == 4:
    os.system("cp ~/.config/qtile/themes/SolarizedDark/colors.py ~/.config/qtile/themes")
    os.system("cp ~/.config/alacritty/themes/SolarizedDark/alacritty.yml ~/.config/alacritty")
    os.system("cp ~/.local/share/rofi/themes/SolarizedDark/onedark.rasi ~/.local/share/rofi/themes")
    os.system("cp ~/.config/dunst/themes/SolarizedDark/dunstrc ~/.config/dunst")
    os.system("qtile cmd-obj -o cmd -f restart")
    os.system("nitrogen --set-zoom-fill --save --random ~/.config/qtile/themes/SolarizedDark/")
    os.system("killall dunst")

# Monokai Pro
elif theme == 5:
    os.system("cp ~/.config/qtile/themes/MonokaiPro/colors.py ~/.config/qtile/themes")
    os.system("cp ~/.config/alacritty/themes/MonokaiPro/alacritty.yml ~/.config/alacritty")
    os.system("cp ~/.local/share/rofi/themes/MonokaiPro/onedark.rasi ~/.local/share/rofi/themes")
    os.system("cp ~/.config/dunst/themes/MonokaiPro/dunstrc ~/.config/dunst")
    os.system("qtile cmd-obj -o cmd -f restart")
    os.system("nitrogen --set-zoom-fill --save --random ~/.config/qtile/themes/MonokaiPro/")
    os.system("killall dunst")

# MaterialOcean
elif theme == 6:
    os.system("cp ~/.config/qtile/themes/MaterialOcean/colors.py ~/.config/qtile/themes")
    os.system("cp ~/.config/alacritty/themes/MaterialOcean/alacritty.yml ~/.config/alacritty")
    os.system("cp ~/.local/share/rofi/themes/MaterialOcean/onedark.rasi ~/.local/share/rofi/themes")
    os.system("cp ~/.config/dunst/themes/MaterialOcean/dunstrc ~/.config/dunst")
    os.system("qtile cmd-obj -o cmd -f restart")
    os.system("nitrogen --set-zoom-fill --save --random ~/.config/qtile/themes/MaterialOcean/")
    os.system("killall dunst")

# TomorrowNight
elif theme == 7:
    os.system("cp ~/.config/qtile/themes/TomorrowNight/colors.py ~/.config/qtile/themes")
    os.system("cp ~/.config/alacritty/themes/TomorrowNight/alacritty.yml ~/.config/alacritty")
    os.system("cp ~/.local/share/rofi/themes/TomorrowNight/onedark.rasi ~/.local/share/rofi/themes")
    os.system("cp ~/.config/dunst/themes/TomorrowNight/dunstrc ~/.config/dunst")
    os.system("qtile cmd-obj -o cmd -f restart")
    os.system("nitrogen --set-zoom-fill --save --random ~/.config/qtile/themes/TomorrowNight/")
    os.system("killall dunst")

# Rxyhn
elif theme == 8:
    os.system("cp ~/.config/qtile/themes/Rxyhn/colors.py ~/.config/qtile/themes")
    os.system("cp ~/.config/alacritty/themes/Rxyhn/alacritty.yml ~/.config/alacritty")
    os.system("cp ~/.local/share/rofi/themes/Rxyhn/onedark.rasi ~/.local/share/rofi/themes")
    os.system("cp ~/.config/dunst/themes/Rxyhn/dunstrc ~/.config/dunst")
    os.system("qtile cmd-obj -o cmd -f restart")
    os.system("nitrogen --set-zoom-fill --save --random ~/.config/qtile/themes/Rxyhn/")
    os.system("killall dunst'")
