# --------------
# Imports modules
from . import user, sudo_password, distroName, initializeModules, Fore, os, Back, Style, getpass, subprocess, re

def changeRootPasswd():

    confirm = input(Fore.WHITE + '\n[x]Do you wanna change ROOT passwd? [x] (y/N): \n')

    if confirm.lower() == "y" and user == "root":
        #sudo_password = getpass.getpass(prompt='Please enter your sudo password: ')
        print(Fore.YELLOW + "### Changing root default pwd ###")

        changeRootPasswd = f'sudo passwd root'
        doChangeRootPasswd = subprocess.Popen(changeRootPasswd, shell=True, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        doChangeRootPasswd_out, doChangeRootPasswd_err = doChangeRootPasswd.communicate()

        if doChangeRootPasswd.returncode == 0:
            print(f'\n')
            print(doChangeRootPasswd_out)
            print(f'\n')
            print(Fore.YELLOW + "Changing ROOT passwd was done!")
            print(f'\n')
            print(f'\n')
        else:
            print(f'\n')
            print(Fore.WHITE + f'{doChangeRootPasswd_err}')
            print(f'\n')
            print(Fore.RED + "Changing ROOT passwd failed :(")
            print(f'\n')
            print(f'\n')
    else:
        print(f'\n')
        print(Fore.WHITE + "NOT gonna change ROOT passwd...\nSkipping...")
        print(f'\n')
        print(f'\n')
    