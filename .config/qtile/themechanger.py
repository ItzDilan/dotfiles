# ------------ Qtile Theme Changer ----------- #

import os

# Menu
def menu():
    print("---------------")
    print("1. DarkGrey")
    print("2. DistroTube")
    print("3. MaterialOcean")
    print("4. MonokaiPro")
    print("5. Rosepine")
    print("6. Nighttime")
    print("---------------")

menu()
theme = int(input("--> "))

# DarkGrey
if theme == 1:
    os.system("nitrogen --set-zoom-fill --save ~/.config/qtile/themes/DarkGrey/'Mascaloona - Dakshin (16-9) (3840 x 2160).jpg'")
    os.system("cp ~/.config/qtile/themes/DarkGrey/colors.py ~/.config/qtile/")

# DistroTube
elif theme == 2:
    os.system("nitrogen --set-zoom-fill --save ~/.config/qtile/themes/DistroTube/PLACES-yacht.jpg")
    os.system("cp ~/.config/qtile/themes/DistroTube/colors.py ~/.config/qtile/")

# MaterialOcean
elif theme == 3:
    os.system("nitrogen --set-zoom-fill --save ~/.config/qtile/themes/MaterialOcean/SweetArch.png")
    os.system("cp ~/.config/qtile/themes/MaterialOcean/colors.py ~/.config/qtile/")

# MonokaiPro
elif theme == 4:
    os.system("nitrogen --set-zoom-fill --save ~/.config/qtile/themes/MonokaiPro/0188.jpg")
    os.system("cp ~/.config/qtile/themes/MonokaiPro/colors.py ~/.config/qtile/")

# Rosepine
elif theme == 5:
    os.system("nitrogen --set-zoom-fill --save ~/.config/qtile/themes/Rosepine/'The Frontier.jpg'")
    os.system("cp ~/.config/qtile/themes/Rosepine/colors.py ~/.config/qtile/")

# Nighttime
elif theme == 6:
    os.system("nitrogen --set-zoom-fill --save ~/.config/qtile/themes/Nighttime/Nighttime.jpeg")
    os.system("cp ~/.config/qtile/themes/Nighttime/colors.py ~/.config/qtile/")
