#!/usr/bin/python3

# Import these for every module component
# --------------
# Imports modules
# --------------
from . import user, sudo_password, distroName, initializeModules, Fore, sys, os, Back, Style, getpass, subprocess, re
# Import module specific variables
from . import thisTime
from . import newUser, newPassword

def addUser():
    # Adding a new privileged user
    addPrivUser = f'echo {sudo_password} | sudo adduser {newUser}'
    doAddPrivUser = subprocess.run(addPrivUser, shell=True, text=True, capture_output=True)
            
    # Changing current password for {newUser} so that he/she can login
    changePassword = f'echo "{newUser}:{newPassword}" | chpasswd'
    doChangePassword = subprocess.run(changePassword, shell=True, text=True, capture_output=True)

    # Adding 'user' to usermod -aG
    usermod = f'echo {sudo_password} | sudo usermod -aG sudo {newUser}'
    doUsermod = subprocess.run(usermod, shell=True, text=True, capture_output=True)


    # Allowing 'user' to run Bash
    print(Fore.YELLOW + f'\nAdding this privileged user:  to Bash runner...\n')
    print(Style.RESET_ALL)
    #addBash = os.system("sudo chsh -s /bin/bash " + user)
    addBash = f'echo {sudo_password} | sudo chsh -s /bin/bash {newUser}'
    doAddBash = subprocess.run(addBash, shell=True, text=True, capture_output=True)


    # Adding 'user' to /ect/sudoers
    addSudoer = f'echo {sudo_password} | sudo echo "{newUser}\tALL=(ALL) ALL" >> /etc/sudoers'
    doAddSudoer = subprocess.run(addSudoer, shell=True, text=True, capture_output=True)


        


    

    
