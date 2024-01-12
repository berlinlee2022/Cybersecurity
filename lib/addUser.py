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
            
    if doAddPrivUser.returncode == 0:
        print(Fore.YELLOW + f'\nAdding this new privileged user has succeeded at {thisTime}!\n')
        print(Fore.YELLOW + f'Terminal output: {doAddPrivUser.stdout}')
        print(Fore.YELLOW + "\nDone! Welcome {}\n".format(newUser))
        print(Style.RESET_ALL)

        # Changing current password for {newUser} so that he/she can login
        changePassword = f'echo "{newUser}:{newPassword}" | chpasswd'
        doChangePassword = subprocess.run(changePassword, shell=True, text=True, capture_output=True)

        if doChangePassword.returncode == 0:
            print(Fore.YELLOW + f'\nSucceeded in creating password for new privileged user: {newUser}!!')
            print(Fore.YELLOW + f'System stdout: {doChangePassword.stdout}')

            print(Fore.WHITE + "\nAdding this new privileged user to Sudoers...")
            print(Style.RESET_ALL)
            # Adding 'user' to usermod -aG
            usermod = f'echo {sudo_password} | sudo usermod -aG sudo {newUser}'
            doUsermod = subprocess.run(usermod, shell=True, text=True, capture_output=True)

            if doUsermod.returncode == 0:
                print(Fore.YELLOW + f'\nSucceeded in changing the usermod for this new privileged user: {newUser}!!\nProceeding to add to Bash runner')
                print(Fore.YELLOW + f'System outputs: {doUsermod.stdout}')
                print(Style.RESET_ALL)

                # Allowing 'user' to run Bash
                print(Fore.YELLOW + f'\nAdding this privileged user:  to Bash runner...\n')
                print(Style.RESET_ALL)
                #addBash = os.system("sudo chsh -s /bin/bash " + user)
                addBash = f'echo {sudo_password} | sudo chsh -s /bin/bash {newUser}'
                doAddBash = subprocess.run(addBash, shell=True, text=True, capture_output=True)


                # Adding 'user' to /ect/sudoers
                addSudoer = f'echo {sudo_password} | sudo echo "{newUser}\tALL=(ALL) ALL" >> /etc/sudoers'
                doAddSudoer = subprocess.run(addSudoer, shell=True, text=True, capture_output=True)

            
            else:
                print(Fore.RED + f'Failed to change usermod for this privileged user: {newUser} :(\nExiting all processes...\n')
                print(Fore.RED + f'System stderr: {doUsermod.stderr}')
                print(Style.RESET_ALL)
                
        # If failed to change password for {newUser}
        else:
            print(Fore.RED + f'\nFailed to create a new password for {newUser}...\nExiting...\n')
            print(Fore.RED + f'System stderr: {doChangePassword.stderr}')
            
    # If failed to create a new priviledged user
    else:
        print(Fore.RED + "\nFailed to add this new privileged user :(\nExiting...\n")
        print(Fore.RED + f'Terminal output: {doAddPrivUser.stdout}')
        print(Fore.RED + f'System stderr for adding {newUser}: {doAddPrivUser.stderr}')
        print(Style.RESET_ALL)

        


    

    
