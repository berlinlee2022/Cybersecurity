# --------------
# Imports modules
# --------------
import os
from colorama import Fore, Back, Style
import subprocess
import getpass

# Update && upgrade Kali repository
def upgrade():

    update = input(Fore.WHITE + "[x] Do you wanna apt update && apt upgrade? [x] (y/N): ")
    print(Style.RESET_ALL)
    if update.lower() == "y":
        user = input(Fore.WHITE + 'Please enter the user to run this script: ')
        sudo_password = getpass.getpass(prompt='Please enter your sudo password: ')
        
        print(Fore.YELLOW + "\nUpdating Kali Linux archive keys...\n")
        print(Style.RESET_ALL)

        print(Fore.YELLOW + "\nItem 1. Updating expried keys on Kali base-build image...\nFrom: https://archive.kali.org/archive-key.asc\nTo: /etc/apt/trusted.gpd.d/kali-archive-keyring.asc\n")
        print(Style.RESET_ALL)
        # Update expired keys on Kali base-build image
        #os.system('sudo wget https://archive.kali.org/archive-key.asc -O /etc/apt/trusted.gpg.d/kali-archive-keyring.asc')
        updateExpiredKeys = f'echo {sudo_password} | sudo wget https://archive.kali.org/archive-key.asc -O /etc/apt/trusted.gpg.d/kali-archive-keyring.asc'

        doUpdateExpiredKeys = subprocess.Popen(updateExpiredKeys, shell=True, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
        doUpdateExpiredKeys.wait()

        if doUpdateExpiredKeys.returncode == 0:
            print(Fore.YELLOW + "*******************************************")
            print(Fore.YELLOW + "\nItem 1. Updating expired keys has succeeded!\n")
            print(Fore.YELLOW + "*******************************************")
            print(Style.RESET_ALL)
        else:
            print(Fore.RED + "Item 1. Updating expried keys on Kali base-build image has failed...\n")
        
        ###
        # Another keys
        print(Fore.YELLOW + "*******************************************")
        print(Fore.YELLOW + "Item 2. Adding new keys \nFrom: https://archive.kali.org/archive-key.asc\nTo: apt-key\nUsing: apt-key add")
        print(Fore.YELLOW + "*******************************************")
        print(Style.RESET_ALL)
        #os.system('sudo wget https://archive.kali.org/archive-key.asc -q -O | apt-key add')
        addAptKey = f'echo {sudo_password} | sudo wget -q -O https://archive.kali.org/archive-key.asc | apt-key add'
        doAddAptKey = subprocess.Popen(addAptKey, shell=True, text=True, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
        doAddAptKey.wait()

        if doAddAptKey.returncode == 0:
            print(Fore.YELLOW + "\nItem 2. Adding new keys has succeeded!\n")

        else:
            print(Fore.RED + "\nItem 2. Adding new keys has failed...\n")
        
        ###
        print(Fore.YELLOW + "*******************************************")
        print(Fore.YELLOW + "\nItem 3. Adding another new keys has succeeded!\n")
        print(Fore.YELLOW + "*******************************************")
        print(Style.RESET_ALL)
        # apt-key directory
        #os.system('sudo apt-key adv --keyserver hkp://keys.gnupg.net --recv-keys 7D8D0BF6')
        addAptKey2 = f'echo {sudo_password} | sudo apt-key adv --keyserver hkp://keys.gnupg.net --recv-keys 7D8D0BF6'
        doAddAptKey2 = subprocess.Popen(addAptKey2, shell=True, text=True, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
        doAddAptKey2.wait()

        if doAddAptKey2.returncode == 0:
            print(Fore.YELLOW + "\nItem 3. Adding another new keys \nFrom: -keyserver hkp://keys.gnupg.net --recv-keys 7D8D0BF6\nUsing: apt-key adv\nhas succeeded!\n")
        else:
            print(Fore.RED + "\nItem 3. Adding another new keys \nFrom: -keyserver hkp://keys.gnupg.net --recv-keys 7D8D0BF6\nUsing: apt-key adv\nhas failed...:(\n")

        ###
        print(Fore.YELLOW + "*******************************************")
        print(Fore.YELLOW + "\nItem4. Updating Kali's repository config file at:\n/etc/apt/sources.list\n")
        print(Fore.YELLOW + "*******************************************")
        print(Style.RESET_ALL)
        # Update Kali.org Repo
        #os.system('sudo echo "deb https://http.kali.org/kali kali-rolling main non-free contrib" > /etc/apt/sources.list')
        # Temporarily changing chmod for /etc/apt/sources.list
        print(Fore.YELLOW + "\nChanging chmod for /etc/apt/sources.list to 777 temporarily...\n")
        chmod = f'echo {sudo_password} | sudo chmod 777 /etc/apt/sources.list'
        doChmod = subprocess.Popen(chmod, shell=True, text=True, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
        doChmod.wait()

        if doChmod.returncode == 0:
            print(Fore.YELLOW + "\nchmod for /etc/apt/sources.list has succeeded!\nProceeding to update Kali Linux repo...\n")

            print(Fore.YELLOW + "\nChanging chown for /etc/apt/sources.list to this scriptRunner temporarily...\n")
            chown = f'echo {sudo_password} | sudo chown {user} /etc/apt/sources.list'
            doChown = subprocess.Popen(chown, shell=True, text=True, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
            doChown.wait()

            if doChown.returncode == 0:
                print(Fore.YELLOW + "\nchown for /etc/apt/sources.list has succeeded!\nProceeding to update Kali Linux repo...\n")

                addDeb = f'echo {sudo_password} | sudo echo "deb https://http.kali.org/kali kali-rolling main non-free contrib" > /etc/apt/sources.list'
                doAddDeb = subprocess.Popen(addDeb, shell=True, text=True, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
                doAddDeb.wait()

                if doAddDeb.returncode == 0:
                    print(Fore.YELLOW + "\ndeb https://http.kali.org/kali kali-rolling main non-free contrib\nhas been successfully added!\n")
                    print(Fore.YELLOW + "*******************************************")
                else:
                    print(Fore.RED + "Failed to add following config to /etc/apt/sources.list ...\ndeb https://http.kali.org/kali kali-rolling main non-free contrib")
        
                addDebSrc = f'echo {sudo_password} | sudo echo "deb-src https://http.kali.org/kali kali-rolling main non-free contrib" >> /etc/apt/sources.list'
                doAddDebSrc = subprocess.Popen(addDebSrc, shell=True, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
                doAddDebSrc.wait()

                if doAddDebSrc.returncode == 0:
                    print(Fore.YELLOW + "\ndeb-src https://http.kali.org/kali kali-rolling main non-free contrib\nhas been successfully added!\n")
                    print(Fore.YELLOW + "*******************************************")
                else:
                    print(Fore.RED + "Failed to add following config to /etc/apt/sources.list ...\ndeb-src https://http.kali.org/kali kali-rolling main non-free contrib")

                # Print /etc/apt/sources.list config
                # No matter changes are made or NOT
                print(Fore.YELLOW + "*******************************************")
                print(Fore.YELLOW + "Current APT config is: \n")
                aptConfig = f'sudo cat /etc/apt/sources.list'
                printAptConfig = subprocess.Popen(aptConfig, shell=True, text=True)
                printAptConfig.wait()
                print(Fore.YELLOW + "*******************************************")
                

                # Update && Upgrade
                print(Fore.YELLOW + "\n\n### Updating & Upgrading Advanced Package Manager ###\n")
                print(Fore.WHITE + "\nDoing apt update && apt upgrade now...\n")
                print(Style.RESET_ALL)
                #os.system('sudo apt update && sudo apt upgrade -yuf')
                updateAndUpgrade = f'echo {sudo_password} | sudo apt update && sudo apt upgrade -yuf'
                doUpdateAndUpgrade = subprocess.Popen(updateAndUpgrade, shell=True)
                doUpdateAndUpgrade.wait()
        
                if doUpdateAndUpgrade.returncode == 0:
                    print(Fore.YELLOW + "\napt has been updated && upgraded successfully!\n")
                    print(Fore.YELLOW + "\nCurrent /etc/apt/sources.list is as following:\n")
                    
                else:
                    print(Fore.RED + "\napt has failed to update => upgrade...\nReasons: \n")

            else: 
                print(Fore.RED + "\nchown for /etc/apt/sources.list has failed...\nNot updating & upgrading apt...\n")

            # Changing chmod for /etc/apt/sources.list back to 644
            print(Fore.YELLOW + "\nChanging chmod for /etc/apt/sources.list back to 644...\n")
            chmod2 = f'echo {sudo_password} | sudo chmod 644 /etc/apt/sources.list'
            doChmod2 = subprocess.Popen(chmod, shell=True, text=True, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
            doChmod2.wait()

            # Changing ownership for /etc/apt/sources.list back to ROOT"
            print(Fore.YELLOW + "\nChanging ownership for /etc/apt/sources.list back to ROOT...\n")
            chown2 = f'echo {sudo_password} | sudo chown root /etc/apt/sources.list'
            doChown2 = subprocess.Popen(chown, shell=True, text=True, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
            doChown2.wait()

        else: 
            print(Fore.RED + "\nchmod for /etc/apt/sources.list has failed...\nNot updating & upgrading apt...\n")
    
    else:
        print(Fore.WHITE + "\nNot doing apt update && apt upgrade -yuf...\nSkipping...\n")

        

        
    