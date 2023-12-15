# --------------
# Imports modules
# --------------
import os
from colorama import Fore, Back, Style
import subprocess
import getpass

def cleanup():
    change = input(Fore.WHITE + "[x] Do you wanna Clean Up APT? [x] (y/N): ")
    if change.lower() == "y":
        user = input(Fore.YELLOW + "Which user are you running this script as: ")
        sudo_password = getpass.getpass("Please enter your sudo password: ")
        print(Fore.YELLOW + "### Cleaning up APT ###")
        print(Style.RESET_ALL)
        #os.system('sudo -u {} sudo apt autoremove -y && sudo apt autoclean -y'.format(user))
        cleanUp = f'echo {sudo_password} | sudo apt autoremove -y && sudo apt autoclean -y'
        doCleanUp = subprocess.Popen(cleanUp, shell=True, text=True)
        doCleanUp.wait()

        if doCleanUp.returncode == 0:
            print(Fore.YELLOW + "\nAPT Cleanup has succeeded!\n")
        else:
            print(Fore.RED + "\nAPT Cleanup has failed...\nSkipping...\n")
    else:
        print(Fore.WHITE + "\nNot gonna APT cleanup...\nSkipping...\n")
# -