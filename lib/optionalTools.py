# --------------
# Imports modules
# --------------
import os
from colorama import Fore, Back, Style
import subprocess
import getpass
# Installing Optional Tools
# --------------
def installOptTools():
    nordVPN = input(
        Fore.GREEN + "[x] Do you want to install NordVPN [x] (y/N): ")
    print(Style.RESET_ALL)
    if nordVPN.lower() == "y":
        print("We are installing it!")
        print(Fore.GREEN + "### Installing NordVPN ###")
        print(Style.RESET_ALL)
        os.system(
            'sudo -u {} sudo wget -qnc https://repo.nordvpn.com/deb/nordvpn/debian/pool/main/nordvpn-release_1.0.0_all.deb'.format(user)
            )
        os.system(
            'sudo -u {} sudo dpkg -i nordvpn-release_1.0.0_all.deb'.format(user))
        os.system(
            'sudo -u {} sudo apt update'.format(user)
            )
        os.system(
            'sudo -u {} sudo apt install nordvpn -y'.format(user))
    else:
        print("Not going to install NordVPN...Skipping...")
# -