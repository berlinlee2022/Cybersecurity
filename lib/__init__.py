#!/usr/bin/python3

import os
import colorama
from colorama import Fore, Back, Style
import subprocess
import getpass
import re
import sys
import time
#import ipcalc

# To confirm Linux distribution in /etc/os-release
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
        return None, None

# Returning user, sudo_password from getCredentials()
user, sudo_password = getCredentials()

def timer():
    try:
        # Retrieve time whenever timer() functions is called
        thisTime = time.localtime(time.time())
        return thisTime

    except Exception as e:
        print(Fore.RED + f'Failed to retrieve current time :(\n')
        return None
thisTime = timer();
    

confirmAddUser = input("Do you wanna add a new priviledged user? [Y/N]: ")
def passingUser():
    
    # Adding a new privileged user
    # Sanity checks
    if confirmAddUser.lower() == 'y' and user.lower() == 'root': 

        newUser = input("Enter new privileged user name: ")
        newPassword = getpass.getpass("Enter your new privileged user password: ")
        confirmNewPassword = getpass.getpass("Enter your new privileged user password: ")

        if newPassword == confirmNewPassword:
            print(Fore.YELLOW + "Will add a new privileged user for you :)")
        else:
            #print(Fore.RED + f'New passwords NOT match!\nExiting...\n')
            return None, None
    else:
        print(Fore.YELLOW + f'NOT gonna add a new priviledged user\nSkipping...\n')
        return None, None
        
    return newUser, newPassword
# Passing newUser, newPassword inputs from passingUser() to this.module
newUser,newPassword = passingUser()

# To update PostgreSQL 15 && 14 TCP ports (5432 && 5433)
confirmUpdatePostgres = input("Do you wanna update PostgreSQL14 & 15 ports 5432? [Y/N]: ")
def passingPostgres():
    if confirmUpdatePostgres.lower() == 'y' and user.lower() == 'root':
        print(Fore.YELLOW + f'Will update postgreSQL 15 & 14 ports :)...\n')
    else:
        print(Fore.YELLOW + f'NOT gonna update postgreSQL 15 & 14 ports\nSkipping...\n')
        return None

    return confirmUpdatePostgres
# Passing confirmUpdatePostgres inputs from passingPostgres() to this.module 
confirmUpdatePostgres = passingPostgres()

# To update http.kali.org => https.kali.org
confirmUpgrade = input("Do you wanna upgrade apt & kali repo? [Y/N]: ")
def passingUpgrade():
    if confirmUpgrade.lower() == 'y' and user.lower() == 'root':
        print(Fore.YELLOW + f'\n\nWill update Kali repository connection using HTTPS\nto allow apt update && apt upgrade\n\n')
        return confirmUpgrade
    else:
        print(Fore.YELLOW + f'\n\nWill NOT update Kali repository\n\nYou have to manually edit Kali repository config file\nhttp://kali.org => https://kali.org\nAND update the Kali keys from Kali archive\nin order to get apt install functions working...\n\n')
        return None
# Passing confirmUpgrade inputs from passingUpgrade() users' inputs to this.module
confirmUpgrade = passingUpgrade()

## For installing open-source tools
confirmInstallTools = input("Do you wanna install tools? [Y/N]: ")
def passingInstallTools():
    if confirmInstallTools.lower() == 'y' and user.lower() == 'root' and newUser:
        print(Fore.YELLOW + f'Will install Open-source tools for you:\nPackage managers\n[e.g. Python3-pip, SNAP, GEM, NixNote2, Nautilus-dropbox, Keepassxc, DNF\n')
        print(Fore.YELLOW + f'Will install Open-source tools: 1N3/Sn1per for you :)\n')
        print(Fore.YELLOW + f'Will install pyautogui for you:)\n')
        print(Fore.YELLOW + f'')
        return confirmInstallTools
    else:
        print(Fore.YELLOW + f'Either {newUser} does NOT exist OR\nScript runner != ROOT OR\nScript runner does NOT want to install open-source tools\nSkipping...\n')
        return None
# Passing confirmInstallTools inputs from passingInstallTools() users' inputs to this.module
confirmInstallTools = passingInstallTools()

## For customizing a NIC
# confirmNetworking = input("Do you wanna configure a network interface? [Y/N]: ")
# def passingNetworking():
#     if confirmNetworking.lower() == 'y' and user.lower() == 'root':
#         print(Fore.YELLOW + f'\nWill set up a NIC for you :)\n')
#         return confirmNetworking
#     else:
#         print(Fore.YELLOW + f'\nNot gonna set up a NIC\nSkipping...\n')
#         return None
# confirmNetworking = passingNetworking()

## For customizing Keyboard Layout
# confirmChangeKeyboardLayout = input("Do you wanna change keyboard layout? [Y/N]: ")
# def passingKeyboard():
#     if confirmChangeKeyboardLayout.lower() == 'y' and user.lower() == 'root':
#         print(Fore.YELLOW + f'\nWill change keyboard layout :)\n')
#         return confirmChangeKeyboardLayout
#     else:
#         print(Fore.YELLOW + f'\nNot gonna change keyboard layout\n')
#         return None
# confirmChangeKeyboardLayout = passingKeyboard()

