# Import these for every module component
# --------------
# Imports modules
# --------------
from . import user, sudo_password, distroName, initializeModules, Fore, sys, os, Back, Style, getpass, subprocess, re
# Import module specific variables
from . import thisTime
from . import user, sudo_password
from . import newUser, newPassword, confirmUpgrade

# Update && upgrade Kali repository
def upgrade():
    if confirmUpgrade.lower() == 'y':
        print(Fore.WHITE + f'******************************************')
        print(Fore.WHITE + f'*****Updating Kali Linux archive keys*****')
        print(Fore.WHITE + f'******************************************')

        print(Fore.YELLOW + f'\nAction 1. Updating expried keys on Kali base-build image\nFrom: https://archive.kali.org/archive-key.asc\nTo: /etc/apt/trusted.gpd.d/kali-archive-keyring.asc\n')
        # Update expired keys on Kali base-build image
        #os.system('sudo wget https://archive.kali.org/archive-key.asc -O /etc/apt/trusted.gpg.d/kali-archive-keyring.asc')
        updateExpiredKeys = f'echo {sudo_password} | sudo wget https://archive.kali.org/archive-key.asc -O /etc/apt/trusted.gpg.d/kali-archive-keyring.asc'

        doUpdateExpiredKeys = subprocess.Popen(updateExpiredKeys, shell=True, text=True)
        doUpdateExpiredKeys.wait()

        if doUpdateExpiredKeys.returncode == 0:
            print(Fore.YELLOW + f'***************************************************************************************************************')
            print(Fore.YELLOW + f'********Succeeded in performing Action 1. Updating expired keys has succeeded at*************\n***{thisTime}***')
            print(Fore.YELLOW + f'***************************************************************************************************************')
        else:
            print(Fore.RED + f'Failed to perform Action 1. Updating expried keys on Kali base-build image at\n{thisTime}\n\n')
            
        ###
        # Another keys
        print(Fore.YELLOW + f'*******************************************************************************************************************')
        print(Fore.YELLOW + f'**************************************Item 2. Adding new keys******************************************************')
        print(Fore.YELLOW + f'***************************From: https://archive.kali.org/archive-key.asc******************************************')
        print(Fore.YELLOW + f'**************************To: apt-key => Using: apt-key add********************************************************')
        print(Fore.YELLOW + f'*******************************************************************************************************************')
        #os.system('sudo wget https://archive.kali.org/archive-key.asc -q -O | apt-key add')
        addAptKey = f'echo {sudo_password} | sudo wget https://archive.kali.org/archive-key.asc | sudo apt-key add'
        doAddAptKey = subprocess.Popen(addAptKey, shell=True, text=True, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
        doAddAptKey.wait()

        if doAddAptKey.returncode == 0:
            print(Fore.YELLOW + f'\nSucceeded in performing Action 2. Adding new keys at\n{thisTime}\n\n')

        else:
            print(Fore.RED + f'\nFailed in performing Action 2. Adding new keys at\n{thisTime}\n\n')
            
        ###
        print(Fore.YELLOW + "*******************************************")
        print(Fore.YELLOW + f'\nSucceeded in performing Action 3. Updating Kali\'s repository config file in:\n/etc/apt/sources.list\nPerformed at:\n{thisTime}\n\n')
        print(Fore.YELLOW + "*******************************************")
        # Update Kali.org Repo
        #os.system('sudo echo "deb https://http.kali.org/kali kali-rolling main non-free contrib" > /etc/apt/sources.list')
        # Temporarily changing chmod for /etc/apt/sources.list
        print(Fore.YELLOW + "\nChanging chmod for /etc/apt/sources.list to 777 temporarily...\n")
        chmod = f'echo {sudo_password} | sudo chmod 777 /etc/apt/sources.list'
        doChmod = subprocess.Popen(chmod, shell=True, text=True, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
        doChmod.wait()

        print(Fore.YELLOW + f'Proceeding to update Kali Linux repo...\n')

        addDeb = f'echo {sudo_password} | sudo printf "deb https://http.kali.org/kali kali-rolling main non-free contrib\ndeb-src https://http.kali.org/kali kali-rolling main non-free contrib" > /etc/apt/sources.list'
        doAddDeb = subprocess.Popen(addDeb, shell=True, text=True, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
        doAddDeb.wait()

        if doAddDeb.returncode == 0:
            print(Fore.YELLOW + f'\nSucceeded in adding below:\ndeb https://http.kali.org/kali kali-rolling main non-free contrib\ndeb-src https://http.kali.org/kali kali-rolling main non-free contrib\nat:\n{thisTime}\n\n')
            print(Fore.YELLOW + "*******************************************")
        else:
            print(Fore.RED + f'Failed to add following config to /etc/apt/sources.list\ndeb-src https://http.kali.org/kali kali-rolling main non-free contrib\nat:\n{thisTime}\n\n')

        # Print /etc/apt/sources.list config
        # No matter changes are made or NOT
        print(Fore.YELLOW + "*******************************************")
        print(Fore.YELLOW + "Current APT config is: \n")
        aptConfig = f'echo {sudo_password} | sudo cat /etc/apt/sources.list'
        printAptConfig = subprocess.Popen(aptConfig, shell=True, text=True)
        printAptConfig.wait()
        print(Fore.YELLOW + "*******************************************")
                    
        # Update && Upgrade
        print(Fore.YELLOW + "##########################################################")
        print(Fore.YELLOW + "\n\n### Updating & Upgrading Advanced Package Manager ###\n")
        print(Fore.WHITE + "\nDoing apt update && apt upgrade now...\n")
        #os.system('sudo apt update && sudo apt upgrade -yuf')
        updateAndUpgrade = f'echo {sudo_password} | sudo apt update && sudo apt upgrade -yuf'
        doUpdateAndUpgrade = subprocess.Popen(updateAndUpgrade, shell=True, text=True)
        doUpdateAndUpgrade.wait()
            
        if doUpdateAndUpgrade.returncode == 0:
            print(Fore.YELLOW + f'\nSucceeded in updating && upgrading APT at:\n{thisTime}\n\n')
            print(Fore.YELLOW + f'\nCurrent /etc/apt/sources.list is as following:\n')
                        
        else:
            print(Fore.RED + f'\nFailed to update && upgrade APT at:\n{thisTime}\n\n')

        # Changing chmod for /etc/apt/sources.list back to 644
        print(Fore.YELLOW + "\nChanging chmod for /etc/apt/sources.list back to 644...\n")
        chmod2 = f'echo {sudo_password} | sudo chmod 644 /etc/apt/sources.list'
        doChmod2 = subprocess.Popen(chmod, shell=True, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        doChmod2.wait()

    else: 
        print(Fore.RED + f'\nFailed to chmod 777 /etc/apt/sources.list at:\n{thisTime}\n\nNot updating & upgrading apt...\n')

        

        
    