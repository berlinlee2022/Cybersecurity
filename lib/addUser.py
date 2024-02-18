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
        doAddPrivUser_out, doAddPrivUser_err = doAddPrivUser.communicate()
        
        if doAddPrivUser.returncode == 0:
            print(f'{doAddPrivUser_out}')
            print(f'\n')
            print(Fore.YELLOW + f'Succeeded in add new Priviledged User :D')            
                
        # Changing current password for {newUser} so that he/she can login
        changePassword = f'echo "{newUser}:{newPassword}" | chpasswd'
        doChangePassword = subprocess.Popen(changePassword, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        doChangePassword_out, doChangePassword_err = doChangePassword.communicate()
        if doChangePassword.returncode == 0:
            print(Fore.WHITE + f'{doChangePassword_out}')
            print(f'\n')
            print(Fore.YELLOW + f'Succeeded in creating the password: {newPassword} for {newUser}\n\n')
            
            # Adding 'user' to usermod -aG
            usermod = f'echo {sudo_password} | sudo usermod -aG sudo {newUser}'
            doUsermod = subprocess.Popen(usermod, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            doUsermod_out, doUsermod_err = doUsermod.communicate()
            if doUsermod.returncode == 0:
                print(Fore.WHITE + f'{doUsermod_out}')
                print(f'\n')
                print(Fore.YELLOW + f'Succeeed in adding {newUser} to sudoers group :D\n\n')
                
                # Allowing 'user' to Popen Bash
                print(Fore.YELLOW + f'\nAdding this new privileged user: {newUser} to Bash group...\n\n')
                #addBash = os.system("sudo chsh -s /bin/bash " + user)
                addBash = f'echo {sudo_password} | sudo chsh -s /bin/bash {newUser}'
                doAddBash = subprocess.Popen(addBash, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
                doAddBash_out, doAddBash_err = doAddBash.communicate()
                
                if doAddBash.returncode == 0:
                    print(Fore.WHITE + f'{doAddBash_out}')
                    print(f'\n')
                    print(Fore.YELLOW + f'Succeeded in adding {newUser} to Bash group\n\n')
                    # Adding 'user' to /ect/sudoers config
                    addSudoer = f'echo {sudo_password} | sudo printf "{newUser}\tALL=(ALL)\tALL" >> /etc/sudoers'
                    doAddSudoer = subprocess.run(addSudoer, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
                    doAddSudoer_out, doAddSudoer_err = doAddSudoer.communicate()
                    if doAddSudoer.returncode == 0:
                        print(Fore.YELLOW + f'Succeeded in adding {newUser} to /etc/sudoer config\n{doAddSudoer_out}')                        
                    else:
                        print(Fore.WHITE + f'{doAddSudoer_err}')
                        print(f'\n')
                        print(Fore.RED + f'Failed to add {newUser} to /etc/sudoers config\nSkipping...\n\n')
                else:
                    print(Fore.WHITE + f'{doAddBash_err}')
                    print(f'\n')
                    print(Fore.RED + f'Failed to add {newUser} to Bash group\n\nSkipping...\n\n')
            else:
                print(Fore.WHITE + f'{doUsermod_err}')
                print(f'\n')
                print(Fore.RED + f'Failed to add {newUser} to sudoers group\n\nSkipping...\n\n')
        else:
            print(Fore.WHITE + f'{doChangePassword_err}')
            print(f'\n')
            print(Fore.RED + f'Failed to create the password for {newUser}\nSkipping...\n\n')
    else:
        print(Fore.WHITE + f'{doAddPrivUser_err}')
        print(f'\n')
        print(Fore.RED + f'Failed to Create New Priviledged User\n\nCould NOT confirm {newUser} OR {newPassword}...\nSkipping...\n\n\n\n\n')


        


    

    
