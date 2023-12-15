# --------------
# Imports modules
from . import user, sudo_password, distroName, initializeModules, Fore, sys, os, Back, Style, getpass, subprocess, re
from . import confirmChangeKeyboardLayout
# --------------

def changeKeyboardLayout():

    if confirmChangeKeyboardLayout.lower() == "y" and user.lower() == "root":
        print(Fore.YELLOW + "*******************")
        print(Fore.YELLOW + "Changing Keyboard Layout")
        print(Fore.YELLOW + "*******************")
        print(Style.RESET_ALL)
        #keyboardUser = input(Fore.WHITE + "Please enter who you're changing keyboard layout for [username]: ")

        changeKeyboard = f'echo {sudo_password} | sudo -u {user} dpkg-reconfigure keyboard-configuration'
        doChangeKeyboard = subprocess.run(changeKeyboard, shell=True, text=True, capture_output=True)

        if doChangeKeyboard.returncode == 0:
            print(Fore.YELLOW + f'Succeeded in changing keyboard layout :D!\nProceeding...\n')
            print(Fore.YELLOW + f'System stdout: {doChangeKeyboard.stdout}')
        else:
            print(Fore.RED + f'Failed to change keyboard layout...\nExiting...\n')
            sys.exit()

    else:
        print(Fore.WHITE + "\nNot gonna change keyboard layout...\nSkipping...\n")

