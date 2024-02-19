# --------------
# Imports modules
# --------------
from . import formatted_time, user, sudo_password, distroName, initializeModules, Fore, sys, os, Back, Style, getpass, subprocess, re
# Import module specific variables
from . import confirmUpgrade
#from . import user, sudo_password

def cleanup(user, sudo_password):

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
        print(Fore.YELLOW + f'Succeeded in Cleaning up APT at:\n{formatted_time}')
        print(f'\n')
        print(f'\n')
    else:
        print(f'\n')
        print(Fore.WHITE + f'{doCleanUp_err}')
        print(f'\n')
        print(Fore.RED + f'Failed to clean up APT\nSkipping at:\n{formatted_time}')
        print(f'\n')
        print(f'\n')
