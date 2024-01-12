# --------------
# Imports modules
# --------------
from . import newUser, sudo_password, distroName, initializeModules, Fore, sys, os, Back, Style, getpass, subprocess, re
# Import module specific variables
from . import thisTime, confirmUpgrade
from . import user, sudo_password

def cleanup():

    if confirmUpgrade.lower() == 'y':
        print(Fore.YELLOW + "########################")
        print(Fore.YELLOW + "### Cleaning up APT ###")
        print(Fore.YELLOW + "########################")
        #os.system('sudo -u {} sudo apt autoremove -y && sudo apt autoclean -y'.format(user))
        cleanUp = f'echo {sudo_password} | sudo apt autoremove -y && sudo apt autoclean -y'
        doCleanUp = subprocess.Popen(cleanUp, shell=True, text=True)
        doCleanUp.wait()

        if doCleanUp.returncode == 0:
            print(Fore.YELLOW + f'\nSucceeded in Cleaning up APT at:\n{thisTime}\n\n')
        else:
            print(Fore.RED + f'\nFailed to clean up APT\nSkipping at:\n{thisTime}\n\n')
    else:
        print(Fore.WHITE + f'\nSkipping apt clean up, as open-source tools were not installed...\n')