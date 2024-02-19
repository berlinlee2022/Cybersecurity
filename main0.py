import os
import colorama
from colorama import Fore, Back, Style
import subprocess
import getpass
import re
import sys
import time
#import ipcalc

# Import all lib
from lib import testCred
#from lib import addUser, updatePostgresql, upgrade, installTools, cleanup

# To confirm Linux distribution in /etc/os-release
def get_distroName():
    try:
        with open('/etc/os-release', 'r') as os_release_file:
            for line in os_release_file:
                if line.startswith('ID='):
                    distro = line.split('=')[1].strip().strip('"')
                    # Extact distribution name and remove quotes
                    return distro
                
    except FileNotFoundError:
        print(Fore.RED + f'Could NOT confirm Linux Distribution...\nSkipping...\n')
        return None

# Move distroName outside the function
distroName = get_distroName()

#distroName = f"Current distro name is: {getDistro}"
#print(Fore.MAGENTA + distroName)
echoDistroName = f"Current distro name is :{distroName}"
print(Fore.MAGENTA + echoDistroName)
print(type(distroName))

# A function to return all essential Python modules
def initializeModules():
    global os, Fore, Back, Style, getpass, subprocess, re

    # Initialize colorama
    colorama.init(autoreset=True)

    return os, Fore, Back, Style, getpass, subprocess, re
    # Initialize all modules

# Getting ROOT priviledge from users to allow sudo actions
def getCredentials():
    try:
        print(Fore.WHITE + "\nProceeding...\n")
        user = input(Fore.WHITE + "Please enter [root]: ")
        sudo_password = getpass.getpass(prompt='Enter sudo password: ')
        return user, sudo_password

    except Exception as e:
        # Handle exceptions
        print(Fore.RED + f'Error retrieving root credentials from script user: {str(e)}')
        print(Fore.RED + 'Terminating script running & all Shell processes...\n')
        sys.exit()

# Returning user, sudo_password from getCredentials()
user, sudo_password = getCredentials()

def timer():
    try:
        # Retrieve time whenever timer() functions is called
        thisTime = time.localtime(time.time())
        return thisTime

    except Exception as e:
        print(Fore.RED + f'Failed to retrieve current time :(\n')
thisTime = timer()

testCred.testCred(user, sudo_password)