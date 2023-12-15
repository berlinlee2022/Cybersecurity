# --------------
# Imports modules
from . import user, sudo_password, distroName, initializeModules, Fore, os, Back, Style, getpass, subprocess, re

def changeRootPasswd():

    confirm = input(Fore.WHITE + '\n[x]Do you wanna change ROOT passwd? [x] (y/N): \n')

    if confirm.lower() == "y" and user == "root":
        #sudo_password = getpass.getpass(prompt='Please enter your sudo password: ')
        print(Fore.YELLOW + "### Changing root default pwd ###")
        print(Style.RESET_ALL)

        #os.system('sudo -u {} sudo passwd root'.format(user))
        changeRootPasswd = f'sudo passwd root'
        doChangeRootPasswd = subprocess.Popen(changeRootPasswd, shell=True)
        doChangeRootPasswd.wait()    

        if doChangeRootPasswd.returncode == 0:
            print(Fore.YELLOW + "Changing ROOT passwd was done!")
            print(doChangeRootPasswd.stdout)
        else:
            print(Fore.RED + "Changing ROOT passwd failed :(")
            print(doChangeRootPasswd.stderr)
    else:
        print(Fore.WHITE + "\nNot gonna change ROOT passwd...\nSkipping...\n")
    