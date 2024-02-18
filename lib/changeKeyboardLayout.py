# --------------
# Imports modules
from . import user, sudo_password, thisTime, distroName, initializeModules, Fore, sys, os, Back, Style, getpass, subprocess, re
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
        doChangeKeyboard = subprocess.Popen(changeKeyboard, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        doChangeKeyboard_out, doChangeKeyboard_err = doChangeKeyboard.communicate()

        if doChangeKeyboard.returncode == 0:
            print(f'\n')
            print(f'{doChangeKeyboard_out}')
            print(f'\n')
            print(f'\n')
            print(Fore.YELLOW + f'Succeeded in changing keyboard layout :D!\nProceeding...')
            print(f'\n')
            print(Fore.YELLOW + f'System stdout: {doChangeKeyboard.stdout}')
            print(f'\n')
            print(f'\n')
        else:
            print(Fore.RED + f'Failed to change keyboard layout...\nExiting...')
            print(f'\n')
            print(f'\n')
            #sys.exit()

    else:
        print(f'\n')
        print(f'\n')
        print(Fore.WHITE + "Not gonna change keyboard layout...\nSkipping...")
        print(f'\n')
        print(f'\n')

