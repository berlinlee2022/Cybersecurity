# Import these for every module component
# --------------
# Imports modules
# --------------
from . import user, sudo_password, distroName, initializeModules, Fore, sys, os, Back, Style, getpass, subprocess, re
# Import module specific variables
from . import thisTime
from . import newUser, newPassword

def addUser():
    if newUser is not None and newPassword is not None:
        # Adding a new privileged user
        addPrivUser = f'echo {sudo_password} | sudo adduser {newUser}'
        doAddPrivUser = subprocess.Popen(addPrivUser, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        doAddPrivUserOut, doAddPrivUserErr = doAddPrivUser.communicate()
        
        if doAddPrivUser.returncode == 0:
            print(f'Succeeded in add new Priviledged User :D')
            print(f'{doAddPrivUserOut}')
                
        # Changing current password for {newUser} so that he/she can login
        changePassword = f'echo "{newUser}:{newPassword}" | chpasswd'
        doChangePassword = subprocess.Popen(changePassword, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        doChangePasswordOut, doChangePasswordErr = doChangePassword.communicate()
        if doChangePassword.returncode == 0:
            print(Fore.YELLOW + f'Succeeded in creating the password: {newPassword} for {newUser}')
            print(f'{doChangePasswordOut}')

            # Adding 'user' to usermod -aG
            usermod = f'echo {sudo_password} | sudo usermod -aG sudo {newUser}'
            doUsermod = subprocess.Popen(usermod, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            doUsermodOut, doUsermodErr = doUsermod.communicate()
            if doUsermod.returncode == 0:
                print(Fore.YELLOW + f'Succeeed in adding {newUser} to sudoers group :D\n{doUsermodOut}')
                
                # Allowing 'user' to Popen Bash
                print(Fore.YELLOW + f'\nAdding this new privileged user: {newUser} to Bash group...\n')
                #addBash = os.system("sudo chsh -s /bin/bash " + user)
                addBash = f'echo {sudo_password} | sudo chsh -s /bin/bash {newUser}'
                doAddBash = subprocess.Popen(addBash, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
                doAddBashOut, doAddBashErr = doAddBash.communicate()
                
                if doAddBash.returncode == 0:
                    print(f'Succeeded in adding {newUser} to Bash group\n{doAddBashOut}')
                    # Adding 'user' to /ect/sudoers config
                    addSudoer = f'echo {sudo_password} | sudo printf "{newUser}\tALL=(ALL)\tALL" >> /etc/sudoers'
                    doAddSudoer = subprocess.run(addSudoer, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
                    doAddSudoerOut, doAddSudoerErr = doAddSudoer.communicate()
                    if doAddSudoer.returncode == 0:
                        print(Fore.YELLOW + f'Succeeded in adding {newUser} to /etc/sudoer config\n{doAddSudoerOut}')                        
                    else:
                        print(Fore.RED + f'Failed to add {newUser} to /etc/sudoers config\nSkipping...')
                else:
                    print(Fore.RED + f'Failed to add {newUser} to Bash group\n{doAddBashErr}\nSkipping...')
            else:
                print(Fore.RED + f'Failed to add {newUser} to sudoers group\n{doUsermodErr}\nSkipping...')
        else:
            print(Fore.RED + f'Failed to create the password for {newUser}\n{doChangePasswordErr}\n\nSkipping...')
    else:
        print(Fore.RED + f'Failed to Create New Priviledged User\n{doAddPrivUserErr}\nCould NOT confirm {newUser} OR {newPassword}...\nSkipping...\n')


        


    

    
