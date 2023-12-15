import os
import colorama
from colorama import Fore, Back, Style
import subprocess
import getpass
import re
import sys
import time
    
def get_distroName():
    try:
        with open('/etc/os-release', 'r') as os_release_file:
            for line in os_release_file:
                if line.startswith('ID='):
                    # Extact distribution name and remove quotes
                    return line.split('=')[1].strip().strip('"')
    except FileNotFoundError:
        return None

# Move distroName outside the function
distroName = get_distroName()
#distroName = f"Current distro name is: {getDistro}"
#print(Fore.MAGENTA + distroName)
echoDistroName = f"Current distro name is :{distroName}"
print(Fore.MAGENTA + echoDistroName)
print(type(distroName))

def initializeModules():
    global os, Fore, Back, Style, getpass, subprocess, re

    # Initialize colorama
    colorama.init(autoreset=True)

    return os, Fore, Back, Style, getpass, subprocess, re
    # Initialize all modules

def getCredentials():
    try:
        print(Fore.WHITE + "\nProceeding...\n")
        user = input(Fore.WHITE + "Please enter [root]: ")
        if user.lower() == "root":
            print(Fore.YELLOW + f'Verifying that your\'re {user}...')
            if os.geteuid() == 0:
                print(Fore.YELLOW + f"Successfully verified that you're root :)!\nProceeding...\n")
            else:
                print(Fore.RED + f'You aren\'t root :(\nExiting process...\n')
                exit()
        
        else:
            print(Fore.RED + f'Sorry, you aren\'t ROOT\nYou can only run this python as ROOT :(')
            exit()

        sudo_password = getpass.getpass(prompt='Enter sudo password: ')
        return user, sudo_password
    except Exception as e:
        # Handle exceptions
        print(Fore.RED + f'Error retrieving root credentials from script user: {str(e)}')
        print(Fore.RED + 'Terminating script running & all Shell processes...\n')
    
user, sudo_password = getCredentials()

### Checking whether script runner wants to execute these processes
confirmAddUser = input("Do you wanna add a new priviledged user? [Y/N]: ")
confirmChangeKeyboardLayout = input("Do you wanna change keyboard layout? [Y/N]: ")
confirmNetworking = input("Do you wanna configure a network interface? [Y/N]: ")
#confirmChangeRootPassword = input("Do you wanna change root password? [Y/N]: ")
# confirmInstallTools = input("Do you wanna install tools? [Y/N]: ")
# confirmOptionalTools = input("Do you wanna install optional tools? [Y/N]: ")
# confirmUpdatePostgres = input("Do you wanna update PostgreSQL14 & 15 ports 5432? [Y/N]: ")
# confirmUpgrade = input("Do you wanna upgrade apt & kali repo? [Y/N]: ")

