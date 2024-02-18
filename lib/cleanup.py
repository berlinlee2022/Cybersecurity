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
        doCleanUp = subprocess.Popen(cleanUp, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        doCleanUp_out, doCleanUp_err = doCleanUp.communicate()

        if doCleanUp.returncode == 0:
            print(f'\n')
            print(Fore.WHITE + f'{doCleanUp_out}')
            print(f'\n')
            print(f'\n')
            print(Fore.YELLOW + f'Succeeded in Cleaning up APT at:\n{thisTime}')
            print(f'\n')
            print(f'\n')
        else:
            print(f'\n')
            print(Fore.WHITE + f'{doCleanUp_err}')
            print(f'\n')
            print(Fore.RED + f'Failed to clean up APT\nSkipping at:\n{thisTime}')
            print(f'\n')
            print(f'\n')
    else:
        print(f'\n')
        print(Fore.WHITE + f'Skipping apt clean up\nBecause confirmUpgrade is: {confirmUpgrade}\n\nOpen-source tools were not installed...')
        print(f'\n')
        print(f'\n')
