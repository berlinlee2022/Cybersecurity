# --------------
# Imports modules
# --------------
from . import newUser, sudo_password, distroName, initializeModules, Fore, sys, os, Back, Style, getpass, subprocess, re
# Import module specific variables
from . import thisTime
from . import user, sudo_password
from . import newUser, newPassword, confirmInstallTools

def installTools():
    if confirmInstallTools is not None and confirmInstallTools.lower() == "y":
        # Default Tools
        print(Fore.YELLOW + "### Installing Default Tools ###")

        # Create directory 'tools'
        print(Fore.YELLOW + "***********************************")
        print(Fore.YELLOW + f'Creating /home/{newUser}/')
        print(Fore.YELLOW + "***********************************")
        createHome = f'echo {sudo_password} | sudo mkdir /home/{newUser}'
        doCreateHome = subprocess.Popen(createHome, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        doCreateHome_out, doCreateHome_err = doCreateHome.communicate()
        if doCreateHome.returncode == 0:
            print(Fore.WHITE + f'{doCreateHome_out}')
            print(f'\n')
            print(f'\n')
        else:
            print(Fore.WHITE + f'{doCreateHome_err}')
            print(f'\n')
            print(f'\n')

        createDesktop = f'echo {sudo_password} | sudo mkdir /home/{newUser}/Desktop'
        doCreateDesktop = subprocess.Popen(createDesktop, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        doCreateDesktop_out, doCreateDesktop_err = doCreateDesktop.communicate()
        if doCreateDesktop.returncode == 0:
            print(f'\n')
            print(Fore.WHITE + f'{doCreateDesktop_out}')
            print(f'\n')
            print(f'\n')
        else:
            print(f'\n')
            print(Fore.WHITE + f'{doCreateDesktop_err}')
            print(f'\n')
            print(f'\n')
            
        createToolsDir = f'echo {sudo_password} | sudo mkdir /home/{newUser}/Desktop/tools'
        doCreateToolsDir = subprocess.Popen(createToolsDir, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        doCreateToolsDir_out, doCreateToolsDir_err = doCreateToolsDir.communicate()
        if doCreateToolsDir.returncode == 0:
            print(f'\n')
            print(Fore.WHITE + f'{doCreateToolsDir_out}')
            print(f'\n')
            print(f'\n')
        else:
            print(f'\n')
            print(Fore.WHITE + f'{doCreateToolsDir_err}')
            print(f'\n')
            print(f'\n')

        change = f'echo {sudo_password} | sudo chmod 777 /home/{newUser}; echo {sudo_password} | sudo chmod 777 /home/{newUser}/Desktop; echo {sudo_password} | sudo chmod 777 /home/{newUser}/Desktop/tools; echo {sudo_password} | sudo chown {newUser} /home/{newUser}; echo {sudo_password} | sudo chown {newUser} /home/{newUser}/Desktop; echo {sudo_password} | sudo chown {newUser} /home/{newUser}/Desktop/tools;'
        doChange = subprocess.Popen(change, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        doChange_out, doChange_err = doChange.communicate()
        if doChange.returncode == 0:
            print(f'\n')
            print(Fore.WHITE + f'{doChange_out}')
            print(f'\n')
            print(f'\n')
        else:
            print(f'\n')
            print(Fore.WHITE + f'{doChange_err}')
            print(f'\n')
            print(f'\n')

        ### Package managers
        print(Fore.YELLOW + "*******************************")
        print(f'\n')
        print(Fore.YELLOW + "Installing package managers\nSNAP\nGEM\nNixNote2\nNautilus-dropbox\nKeepassxc\nPython3-pip\nDNF")
        print(f'\n')
        print(f'\n')
        installPackage = f'echo {sudo_password} | sudo apt install snapd gem nixnote2 nautilus-dropbox keepassxc python3-pip dnf -y'
        doInstallPackage = subprocess.Popen(installPackage, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        doInstallPackage_out, doInstallPackage_err = doInstallPackage.communicate()

        if doInstallPackage.returncode == 0:
            print(f'\n')
            print(Fore.WHITE + f'{doInstallPackage_out}')
            print(Fore.YELLOW + f'\nInstallation of package managers has succeeded at\n{thisTime}!')
            print(f'\n')
            print(f'\n')
        else:
            print(f'\n')
            print(Fore.WHITE + f'{doInstallPackage_err}')
            print(f'\n')
            print(Fore.RED + f'Failed to install of package managers has failed at\n{thisTime}:(')
            print(f'\n')
            print(f'\n')

        # Installing pyautogui
        print(Fore.YELLOW + "\nInstalling pyautogui...\n")
        installPyautogui = f'pip3 install pyautogui'
        doInstallPyautogui = subprocess.Popen(installPyautogui, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        doInstallPyautogui_out, doInstallPyautogui_err = doInstallPyautogui.communicate()

        if doInstallPyautogui.returncode == 0:
            print(f'\n')
            print(f'{doInstallPyautogui_out}')
            print(f'\n')
            print(Fore.YELLOW + f'Installation of pyautogui has succeeded!')
            print(f'\n')
            print(f'\n')
        else:
            print(f'\n')
            print(Fore.WHITE + f'{doInstallPyautogui_err}')
            print(f'\n')
            print(Fore.RED + "Failed to install pyautogui...:(\nPackage manager python3-pip might not be installed correctly :(\nSkipping...")
            print(f'\n')
            print(f'\n')

        ### Recon tools
        print(f'\n')
        print(Fore.YELLOW + "### Installing recon tools...###")
        print(f'\n')
        path = f'/home/{newUser}/Desktop/tools/'
        
        # Downloading Sn1per
        print(Fore.YELLOW + "\nInstalling Sn1per...\n")
        downloadSn1per = f'echo {sudo_password} | sudo git clone https://github.com/1N3/Sn1per.git;' 
        doDownloadSn1per = subprocess.Popen(downloadSn1per, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        doDownloadSn1per_out, doDownloadSn1per_err = doDownloadSn1per.communicate()
        if doDownloadSn1per.returncode == 0:
            print(f'\n')
            print(Fore.WHITE + f'{doDownloadSn1per_out}')
            print(f'\n')
            print(Fore.YELLOW + f'1N3/Sn1per has been downloaded successfully!')
            print(f'\n')
            print(f'Please cd ~/{newUser}/Desktop/tools/Sn1per => sudo bash Download.sh')
            print(f'\n')
            print(f'Proceeding to change Sn1per folder permissions...')
            print(f'\n')
            print(f'\n')
        else:
            print(f'\n')
            print(f'{doDownloadSn1per_err}')
            print(f'\n')
            print(Fore.RED + f'Failed to download Sn1per :(')
            print(f'\n')
            print(f'\n')
                  
        changeSn1perPermission = f'echo {sudo_password} | sudo chown {newUser} {path}S1nper; echo {sudo_password} | sudo chmod 777 {newUser} {path}Sn1per; echo {sudo_password} | sudo chown {newUser} {path}Sn1per/install.sh; echo {sudo_password} | sudo chmod 777 {newUser} {path}Sn1per/install.sh'
        doChangeSn1perPermission = subprocess.Popen(changeSn1perPermission, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        doChangeSn1perPermission_out, doChangeSn1perPermission_err = doChangeSn1perPermission_out.communicate()

        if doChangeSn1perPermission.returncode == 0:
            print(f'\n')
            print(Fore.WHITE + f'{doChangeSn1perPermission_out}')
            print(f'\n')
            print(Fore.YELLOW + f'Succeeded in changing Sn1per ownership to {newUser} at\n{thisTime}')
            print(f'\n')
            print(Fore.YELLOW + f'Please proceed to {path}Sn1per/install.sh for installation :)...')
            print(f'\n')
            print(f'\n')
        else:
            print(f'\n')
            print(Fore.WHITE + f'{doChangeSn1perPermission_err}')
            print(Fore.RED + f'Failed to change Sn1per ownership to {newUser}...\nSkipping...')
            print(f'\n')
            print(f'\n')                
            
        #Downloading Sherlock
        print(Fore.YELLOW + "\nDownloading Sherlock...\n")
        downloadSherlock = f'echo {sudo_password} | sudo git clone https://github.com/sherlock-project/sherlock.git'
        doDownloadSherlock = subprocess.Popen(downloadSherlock, shell=True, text=True)
        doDownloadSherlock_out, doDownloadSherlock_err = doDownloadSherlock.communciate()

        if doDownloadSherlock.returncode == 0:
            print(f'\n')
            print(Fore.WHITE + f'{doDownloadSherlock_out}')
            print(f'\n')
            print(Fore.YELLOW + f'Downloadation of Sherlock has succeeded at\n{thisTime}!\n\nProceeding to change Sherlock folder permissions at\n{thisTime}\n\n')
            print(f'\n')
        else:
            print(f'\n')
            print(Fore.RED + f'{doDownloadSherlock_err}')
            print(f'\n')
            print(f'\n')
        
        changeSherlockPermission = f'echo {sudo_password} | sudo chown {newUser} {path}sherlock; echo {sudo_password} | sudo chmod 777 {newUser} {path}sherlock; echo {sudo_password} | sudo chown {newUser} {path}sherlock;'
        doChangeSherlockPermission = subprocess.Popen(changeSherlockPermission, shell=True, text=True)
        doChangeSherlockPermission_out, doChangeSherlockPermission_err = doChangeSherlockPermission.communicate()

        if doChangeSherlockPermission.returncode == 0:
            print(f'\n')
            print(Fore.WHITE + f'{doChangeSherlockPermission_out}')
            print(f'\n')
            print(Fore.YELLOW + f'Succeeded in changing Sherlock ownership to {newUser} at\n{thisTime}')
            print(f'\n')
            print(Fore.YELLOW + f'Please proceed to {path}Sherlock/install.sh for installation :)')
            print(f'\n')
            print(f'\n')
        else:
            print(f'\n')
            print(Fore.WHITE + f'{doChangeSherlockPermission_err}')
            print(f'\n')
            print(Fore.RED + f'Failed to change Sherlock ownership to {newUser}...\nSkipping...')
            print(f'\n')
            print(f'\n')

        # Installing RedHawk
        print(f'\n')
        print(Fore.YELLOW + "Downloading RedHawk...")
        print(f'\n')
        installRedHawk = f'echo {sudo_password} | sudo git clone https://github.com/Tuhinshubhra/RED_HAWK.git'
        doInstallRedHawk = subprocess.Popen(installRedHawk, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        doInstallRedHawk_out, doInstallRedHawk_err = doInstallRedHawk.communicate()

        if doInstallRedHawk.returncode == 0:
            print(f'\n')
            print(Fore.WHITE + f'{doInstallRedHawk_out}')
            print(Fore.YELLOW + "Installation of RedHawk has succeeded!\nProceeding to change permissions...")
            print(f'\n')
        else:
            print(f'\n')
            print(Fore.WHITE + f'{doInstallRedHawk_err}')
            print(Fore.RED + f'Failed to download RedHawk :(')
            print(f'\n')
            print(f'\n')
        
        changeRedHawkPermissions = f'echo {sudo_password} | sudo chown {newUser} {path}RED_HAWK; echo {sudo_password} | sudo chmod 777 {newUser} {path}RED_HAWK;'
        doChangeRedHawkPermissions = subprocess.Popen(changeRedHawkPermissions, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        doChangeRedHawkPermissions_out, doChangeRedHawkPermissions_err = doChangeRedHawkPermissions.communicate()
        if doChangeRedHawkPermissions.returncode == 0:
            print(Fore.YELLOW + f'Succeeded in changing RED_HAWK ownership & permissions!\n')
        else:
            print(f'\n')
            print(Fore.WHITE + f'{doChangeRedHawkPermissions_err}')
            print(Fore.RED + f'Failed to change ownership & permissions for RED_HAWK...\nSkipping...')        
            print(f'\n')
            print(f'\n')

        # Installing SecLists
        print(Fore.YELLOW + "\nInstalling Seclist...\n")
        installSeclist = f'cd {path} && echo {sudo_password} | sudo git clone https://github.com/danielmiessler/SecLists.git'
        doInstallSeclist = subprocess.Popen(installSeclist, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        doInstallSeclist_out, doInstallSeclist_err = doInstallSeclist.communicate()

        if doInstallSeclist.returncode == 0:
            print(f'\n')
            print(Fore.WHITE + f'{doInstallSeclist_out}')
            print(f'\n')
            print(Fore.YELLOW + f'\nInstallation of Seclist has succeeded at\n{thisTime}')
            print(f'\n')
            print(f'\n')
        else:
            print(f'\n')
            print(f'{doInstallSeclist_err}')
            print(f'\n')
            print(Fore.RED + f'\nFailed to install Seclist at\n{thisTime}')
            print(f'\n')
            print(f'\n')
                
        # Install EyeWitness
        print(Fore.YELLOW + "### Installing EyeWitness ###")
        print(Style.RESET_ALL)
        installEyewitness = f'cd {path} && echo {sudo_password} | sudo git clone https://github.com/RedSiege/EyeWitness.git'
        doInstallEyewitness = subprocess.Popen(installEyewitness, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        doInstallEyewitness_out, doInstallEyewitness_err = doInstallEyewitness.communicate()

        if doInstallEyewitness.returncode == 0:
            print(f'\n')
            print(Fore.WHITE + f'{doInstallEyewitness_out}')
            doInstallEyewitness
            print(Fore.YELLOW + f'Succeeded in downloading EyeWitness at\n{thisTime}')
            print(f'\n')
        else:
            print(f'\n')
            print(Fore.RED + f'{doInstallEyewitness_err}')
            print(f'\n')
            
        changeEyeWitnessPermission = f'echo {sudo_password} | sudo chown {newUser} {path}EyeWitness; echo {sudo_password} | sudo chmod 777 {path}EyeWitness;'
        doChangeEyeWitnessPermission = subprocess.Popen(changeEyeWitnessPermission, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        doChangeEyeWitnessPermission_out, doChangeEyeWitnessPermission_err = doChangeEyeWitnessPermission.communicate()
        if doChangeEyeWitnessPermission.returncode == 0:
            print(f'\n')
            print(Fore.WHITE + f'{doChangeEyeWitnessPermission_out}')
            print(f'\n')
            print(Fore.YELLOW + f'Succeeded in changing permission for {path}EyeWitness at\n{thisTime}')
            print(f'\n')
            print(f'\n')
        else:
            print(f'\n')
            print(f'{doChangeEyeWitnessPermission_err}')
            print(f'\n')
            print(Fore.RED + f'Failed to change permissions for {path}EyeWitness at\n{thisTime}\nSkipping...')
            print(f'\n')
            print(f'\n')

        # Install Evil-WinRM
        print(Fore.YELLOW + "### Installing Evil-WinRM ###")
        print(f'\n')
        installEvilwinrm = f'echo {sudo_password} | sudo git clone https://github.com/Hackplayers/evil-winrm.git'
        doInstallEvilwinrm = subprocess.Popen(installEvilwinrm, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        doInstallEvilwinrm_out, doInstallEvilwinrm_err = doInstallEvilwinrm.communicate()

        if doInstallEvilwinrm.returncode == 0:
            print(f'\n')
            print(Fore.WHITE + f'{doInstallEvilwinrm_out}')
            print(f'\n')
            print(Fore.YELLOW + f'Succeeded in downloading Evil-WinRM at {path}\nProceeding to change permissions for {path}EyeWitness')
            print(f'\n')
            print(f'\n')
        else:
            print(f'\n')
            print(Fore.WHITE + f'{doInstallEvilwinrm_err}')
            print(f'\n')
            print(f'\n')
        
        changeEvilWinRm = f'echo {sudo_password} | sudo chown {newUser} {path}evil-winrm; echo {sudo_password} | sudo chmod 777 {path}evil-winrm;'
        doChangeEvilWinRm = subprocess.Popen(changeEvilWinRm, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        doChangeEvilWinRm_out, doChangeEvilWinRm_err = doChangeEvilWinRm.communicate()
        if doChangeEvilWinRm.returncode == 0:
            print(f'\n')
            print(Fore.WHITE + f'{doChangeEvilWinRm_out}')
            print(f'\n')
            print(f'\n')
        else:
            print(f'\n')
            print(Fore.WHITE + f'{doChangeEvilWinRm_err}')
                    
        # Install Powerline
        print(Fore.YELLOW + "### Installing Powerline ###")
        print(Style.RESET_ALL)
        installPowerline = f'cd {path} && echo {sudo_password} | sudo git clone https://github.com/powerline/powerline.git'
        doInstallPowerline = subprocess.Popen(installPowerline, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        doInstallPowerline_out, doInstallPowerline_err = doInstallPowerline.communicate()

        if doInstallPowerline.returncode == 0:
            print(f'\n')
            print(Fore.WHITE + f'{doInstallPowerline_out}')
            print(f'\n')
            print(Fore.YELLOW + f'Succeeded in downloading Powerline at {path} at\n{thisTime}')
            print(f'\n')
            print(f'\n')
        else:
            print(f'\n')
            print(Fore.WHITE + f'{doInstallPowerline_err}')
            print(f'\n')
            print(f'\n')
        
        changePowerLine = f'echo {sudo_password} | sudo chown {newUser} {path}powerline; echo {sudo_password} | sudo chmod 777 {path}powerline'
        doChangePowerLine = subprocess.Popen(changePowerLine, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        doChangePowerLine_out, doChangePowerLine_err = doChangePowerLine.communicate()
                    
        if doChangePowerLine.returncode == 0:
            print(f'\n')
            print(Fore.WHITE + f'{doChangePowerLine_out}')
            print(f'\n')
            print(f'\n')
        else:
            print(f'\n')
            print(Fore.WHITE + f'{doChangePowerLine_err}')
            print(f'\n')
            print(f'\n')
            
        # Install BeefProject
        print(Fore.YELLOW + "### Installing Beef-XSS ###")
        print(Style.RESET_ALL)
        #os.system('sudo -u {} sudo apt install beef-xss -y'.format(newUser))
        beefXSSPath = f'/home/{newUser}/Desktop/tools/beef-xss/'
        installBeefXSS = f'echo {sudo_password} | sudo apt install beef-xss -y'
        doInstallBeefXSS = subprocess.Popen(installBeefXSS, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        doInstallBeefXSS_out, doInstallBeefXSS_err = doInstallBeefXSS.communicate()

        if doInstallBeefXSS.returncode == 0:
            print(f'\n')
            print(Fore.WHITE + f'{doInstallBeefXSS_out}')
            print(f'\n')
            print(Fore.YELLOW + f'Succeeded in installing Beef-XSS at\n{thisTime}')
            print(f'\n')
            print(f'\n')
        else:
            print(f'\n')
            print(Fore.WHITE + f'{doInstallBeefXSS_err}')
            print(f'\n')
            print(Fore.RED + f'Failed to install Beef-XSS :(\Skipping...')
            print(f'\n')
            print(f'\n')
        
        print(Fore.YELLOW + f'\nEnabling Beef-XSS binary at\n{thisTime}...')
        enableBeefXSS = f'echo {sudo_password} | sudo systemctl enable beef-xss'
        doEnableBeefXSS = subprocess.Popen(enableBeefXSS, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        doEnableBeefXSS_out, doEnableBeefXSS_err = doEnableBeefXSS.communicate()
                
        if doEnableBeefXSS.returncode == 0:
            print(f'\n')
            print(f'{doEnableBeefXSS_out}')
            print(f'\n')
            print(Fore.YELLOW + f'Succeeded in enabling Beef-XSS\nStarting up Beef-XSS!')
            print(f'\n')
            print(f'\n')
        else:
            print(f'\n')
            print(Fore.WHITE + f'{doEnableBeefXSS_err}')
            print(f'\n')
            print(Fore.RED + f'Failed to enable Beef-XSS :(\nSkipping...')
            print(f'\n')
            print(f'\n')
        
        startBeefXSS = f'echo {sudo_password} | sudo systemctl start beef-xss'
        doStartBeefXSS = subprocess.Popen(startBeefXSS, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        doStartBeefXSS_out, doStartBeefXSS_err = doStartBeefXSS.communicate()
                    
        if doStartBeefXSS.returncode == 0:
            print(f'\n')
            print(Fore.WHITE + f'{doStartBeefXSS_out}')
            print(f'\n')
            print(Fore.YELLOW + f'Succeeded in starting up Beef-XSS at\n{thisTime}\nProceeding to configure Beef-XSS!')
            print(f'\n')
            print(f'\n')
        else:
            print(f'\n')
            print(Fore.WHITE + f'{doStartBeefXSS_err}')
            print(f'\n')
            print(Fore.RED + f'Failed to start Beef-XSS :(\nSkipping')
            print(f'\n')
            print(f'\n')
        
        # Locate Beef-XSS config file
        # Save it to var $beefDir                        
        print(Fore.YELLOW + f'Changing Beef-XSS login credentials...')
        print(f'\n')
        #beefnewUser = input(Fore.YELLOW + "Enter new newUsername for Beef-XSS UI login: ")
        editLoginCommand = f'echo {sudo_password} | sudo sed -i \'s/newUser\: beef/newUser\: {newUser}/g\' /etc/beef-xss/config.yaml; echo {sudo_password} | sudo sed -i \'s/passwd\: beef/passwd\: {newPassword}/g\' /etc/beef-xss/config.yaml'
        doEditLogin=subprocess.Popen(editLoginCommand, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        doEditLogin_out, doEditLogin_err = doEditLogin.communicate()
                        
        if doEditLogin.returncode == 0:
            print(f'\n')
            print(f'{doEditLogin_out}')
            print(Fore.YELLOW + f'\nSucceeded in changing Beef-XSS Login credentials in /etc/beef-xss/config.yaml at\n{thisTime}')
            print(f'\n')
            print(f'\n')
        else:
            print(f'\n')
            print(Fore.WHITE + f'{doEditLogin_err}')
            print(f'\n')
            print(f'\n')
        
        ### Creating a directory to store current Beef-XSS Login credentials
        print(Fore.YELLOW + f'Creating a directory:\n{beefXSSPath}\nTo store current Beef-XSS Login credentials')
        print(f'\n')
        createLoginCommand = f'echo {sudo_password} | sudo mkdir {beefXSSPath}'
        doCreateLogin=subprocess.Popen(createLoginCommand, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        doCreateLogin_out, doCreateLogin_err = doCreateLogin.communicate()
                            
        if doCreateLogin.returncode == 0:
            print(f'\n')
            print(Fore.WHITE + f'{doCreateLogin_out}')
            print(f'\n')
            print(Fore.YELLOW + f'Succeeded in creating a directory for Beef-XSS Login credentials file at\n{thisTime}')
            print(f'\n')
            print(f'\n')
        else:
            print(f'\n')
            print(Fore.WHITE + f'{doCreateLogin_err}')
            print(f'\n')
            print(Fore.RED + f'Failed to create a directory for Beef-XSS Login credentials file at\n{thisTime}')
            print(f'\n')
            print(f'\n')
        
        purgeLoginTxt = f'echo {sudo_password} | sudo rm -rf {beefXSSPath}login.txt;'
        doPurgeLoginTxt=subprocess.Popen(purgeLoginTxt, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        doPurgeLoginTxt_out, doPurgeLoginTxt_err = doPurgeLoginTxt.communicate()
        
        if doPurgeLoginTxt.returncode == 0:
            print(f'\n')
            print(f'{doPurgeLoginTxt_out}')
            print(f'\n')
            print(Fore.YELLOW + f'\nSucceeded in purging existing Login credentials file in {beefXSSPath} at\n{thisTime}\n')
            print(f'\n')
            print(f'\n')
        else:
            print(f'\n')
            print(Fore.WHITE + f'{doPurgeLoginTxt_err}')
            print(f'\n')
            print(Fore.RED + f'\nFailed to purge existing Login credentials in {beefXSSPath}\nSkipping...')
            print(f'\n')
            print(f'\n')
        
        print(Fore.YELLOW + f'\nCreating login.txt in {beefXSSPath}login.txt at\n{thisTime}\n')
        createLoginTxt = f'echo {sudo_password} | sudo touch {beefXSSPath}login.txt; echo {sudo_password} | sudo chmod 400 {beefXSSPath}login.txt; echo {sudo_password} | sudo chown {newUser} {beefXSSPath}login.txt;'
        doCreateLoginTxt = subprocess.Popen(createLoginTxt, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        doCreateLoginTxt_out, doCreateLoginTxt_err = doCreateLoginTxt.communicate()
                                
        if doCreateLoginTxt.returncode == 0:
            print(f'\n')
            print(Fore.WHITE + f'{doCreateLoginTxt_out}')
            print(Fore.YELLOW + f'\nSucceeded in creating Login credentials in {beefXSSPath}login.txt at\n{thisTime}')
            print(f'\n')
            print(f'\n')
        else:
            print(f'\n')
            print(Fore.WHITE + f'{doCreateLoginTxt_err}')
            print(f'\n')
            print(Fore.RED + f'Failed to create Login credentials in {beefXSSPath}login.txt :(')
            print(f'\n')
            print(f'\n')
    
        # Verifying Beef-XSS login credentials changes
        print(Fore.YELLOW + f'\nSaving the current Beef-XSS login credentials...\n')
        saveLogin = f'newUser=$(echo {sudo_password} | sudo egrep "\s+{newUser}\:\s+(.*)" /etc/beef-xss/config.yaml); passwd=$(echo {sudo_password} | sudo egrep "\s+passwd\:\s+(.*)" /etc/beef-xss/config.yaml); echo {sudo_password} | sudo echo $newUser > {beefXSSPath}login.txt; echo {sudo_password} | sudo echo $passwd >> {beefXSSPath}login.txt;'
        doSaveLogin = subprocess.Popen(saveLogin, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        doSaveLogin_out, doSaveLogin_err = doSaveLogin.communicate()
                                    
        if doSaveLogin.returncode == 0:
            print(f'\n')
            print(Fore.WHITE + f'{doSaveLogin_out}')
            print(f'\n')
            print(Fore.YELLOW + f'\nSucceeded in saving current Beef-XSS Login credentials at\n{thisTime}\nPlease cat {beefXSSPath}login.txt for your login credentials :)')
            print(f'\n')
            print(f'\n')
        else:
            print(f'\n')
            print(Fore.WHITE + f'{doSaveLogin_err}')
            print(f'\n')
            print(Fore.RED + f'Failed to save current Beef-XSS Login credentials at\n{thisTime}\nSkipping...')
            print(f'\n')
            print(f'\n')
        
        # Restart Beef-XSS
        print(Fore.YELLOW + f'\nRestarting Beef-XSS...\n')
        restartBeefXSS = f'echo {sudo_password} | sudo systemctl restart beef-xss'
        doRestartBeefXSS = subprocess.Popen(restartBeefXSS, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        doRestartBeefXSS_out, doRestartBeefXSS_err = doRestartBeefXSS.communicate()
                                        
        if doRestartBeefXSS.returncode == 0:
            print(f'\n')
            print(Fore.WHITE + f'{doRestartBeefXSS_out}')
            print(f'\n')
            print(Fore.YELLOW + f'\nSucceeded in restarting Beef-XSS at\n{thisTime}')
            print(f'\n')
            print(Fore.YELLOW + f'\n\nBeef-XSS is now accessible at http://127.0.0.1:3000/ui/authentication')
            print(f'\n')
            print(f'\n')
        else:
            print(f'\n')
            print(Fore.WHITE + f'{doRestartBeefXSS_err}')
            print(Fore.RED + f'\nFailed to restart Beef-XSS...\nYou may restart Beef-XSS yourself then to login using your credentials in {beefXSSPath}login.txt\nat http://127.0.0.1:3000/ui/authentication\nSkipping...')
            print(f'\n')
            print(f'\n')
    
    else:
        print(f'\n')        
        print(Fore.WHITE + f'NOT gonna Install any Tools\nSkipping...')
        print(f'\n')
        print(f'\n')
        print(f'\n')
        print(f'\n')
                  
 