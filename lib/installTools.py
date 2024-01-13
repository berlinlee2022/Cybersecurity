# --------------
# Imports modules
# --------------
from . import newUser, sudo_password, distroName, initializeModules, Fore, sys, os, Back, Style, getpass, subprocess, re
# Import module specific variables
from . import thisTime
from . import user, sudo_password
from . import newUser, newPassword, confirmInstallTools

def installTools():
    if confirmInstallTools.lower() == "y":
        # Default Tools
        print(Fore.YELLOW + "### Installing Default Tools ###")

        # Create directory 'tools'
        print(Fore.YELLOW + "***********************************")
        print(Fore.YELLOW + f'Creating /home/{newUser}/Desktop/tools')
        print(Fore.YELLOW + "***********************************")
        print(Style.RESET_ALL)
        createHome = f'echo {sudo_password} | sudo mkdir /home/{newUser}'
        doCreateHome = subprocess.Popen(createHome, shell=True, text=True)
        doCreateHome.wait()

        createDesktop = f'echo {sudo_password} | sudo mkdir /home/{newUser}/Desktop'
        doCreateDesktop = subprocess.Popen(createDesktop, shell=True, text=True)
        doCreateDesktop.wait()
        createToolsDir = f'echo {sudo_password} | sudo mkdir /home/{newUser}/Desktop/tools'
        doCreateToolsDir = subprocess.Popen(createToolsDir, shell=True, text=True)
        doCreateToolsDir.wait()

        change = f'echo {sudo_password} | sudo chmod 777 /home/{newUser}; echo {sudo_password} | sudo chmod 777 /home/{newUser}/Desktop; echo {sudo_password} | sudo chmod 777 /home/{newUser}/Desktop/tools; echo {sudo_password} | sudo chown {newUser} /home/{newUser}; echo {sudo_password} | sudo chown {newUser} /home/{newUser}/Desktop; echo {sudo_password} | sudo chown {newUser} /home/{newUser}/Desktop/tools;'
        doChange = subprocess.Popen(change, shell=True, text=True)
        doChange.wait()
        #os.system('sudo mkdir /home/phoenix/Desktop/tools')

        ### Package managers
        print(Fore.YELLOW + "*******************************")
        print(Fore.YELLOW + "\nInstalling package managers\nSNAP\nGEM\nNixNote2\nNautilus-dropbox\nKeepassxc\nPython3-pip\nDNF\n")
        installPackage = f'echo {sudo_password} | sudo apt install snapd gem nixnote2 nautilus-dropbox keepassxc python3-pip dnf -y'
        doInstallPackage = subprocess.Popen(installPackage, shell=True, text=True)
        doInstallPackage.wait()

        if doInstallPackage.returncode == 0:
            print(Fore.YELLOW + f'\nInstallation of package managers has succeeded at\n{thisTime}!\n')
        else:
            print(Fore.RED + f'\nFailed to install of package managers has failed at\n{thisTime}:(\n')

        # Installing pyautogui
        print(Fore.YELLOW + "\nInstalling pyautogui...\n")
        installPyautogui = f'pip3 install pyautogui'
        doInstallPyautogui = subprocess.Popen(installPyautogui, shell=True, text=True)
        doInstallPyautogui.wait()

        if doInstallPyautogui.returncode == 0:
            print(Fore.YELLOW + f'\nInstallation of pyautogui has succeeded!\n')
        else:
            print(Fore.RED + "\nFailed to install pyautogui...:(\nPackage manager python3-pip might not be installed correctly :(\nSkipping...\n")

        ### Recon tools
        print(Fore.YELLOW + "\n### Installing recon tools...###\n")
        path = f'/home/{newUser}/Desktop/tools/'
        # Installing Sn1per
        print(Fore.YELLOW + "\nInstalling Sn1per...\n")
        installSn1per = f'echo {sudo_password} | sudo git clone https://github.com/1N3/Sn1per.git;' 
        doInstallSn1per = subprocess.Popen(installSn1per, shell=True, text=True)
        doInstallSn1per.wait()

        if doInstallSn1per.returncode == 0:
            print(Fore.YELLOW + f'1N3/Sn1per has been downloaded successfully!\nPlease cd ~/{newUser}/Desktop/tools/Sn1per => sudo bash install.sh\nProceeding to change Sn1per folder permissions...\n')
            changeSn1perPermission = f'echo {sudo_password} | sudo chown {newUser} {path}S1nper; echo {sudo_password} | sudo chmod 777 {newUser} {path}Sn1per; echo {sudo_password} | sudo chown {newUser} {path}Sn1per/install.sh; echo {sudo_password} | sudo chmod 777 {newUser} {path}Sn1per/install.sh'
            doChangeSn1perPermission = subprocess.Popen(changeSn1perPermission, shell=True, text=True)
            doChangeSn1perPermission.wait()

            if doChangeSn1perPermission.returncode == 0:
                print(Fore.YELLOW + f'Succeeded in changing Sn1per ownership to {newUser} at\n{thisTime}\nPlease proceed to {path}Sn1per/install.sh for installation :)...\n')
            else:
                print(Fore.RED + f'Failed to change Sn1per ownership to {newUser}...\nSkipping...\n')
                
        else:
            print(Fore.RED + "\nSn1per has NOT been downloaded successfully...:(\n")
            
        #Downloading Sherlock
        print(Fore.YELLOW + "\nDownloading Sherlock...\n")
        installSherlock = f'echo {sudo_password} | sudo git clone https://github.com/sherlock-project/sherlock.git'
        doInstallSherlock = subprocess.Popen(installSherlock, shell=True, text=True)
        doInstallSherlock.wait()

        if doInstallSherlock.returncode == 0:
            print(Fore.YELLOW + f'Installation of Sherlock has succeeded at\n{thisTime}!\nProceeding to change Sherlock folder permissions at\n{thisTime}')
            changeSherlockPermission = f'echo {sudo_password} | sudo chown {newUser} {path}sherlock; echo {sudo_password} | sudo chmod 777 {newUser} {path}sherlock; echo {sudo_password} | sudo chown {newUser} {path}sherlock;'
            doChangeSherlockPermission = subprocess.Popen(changeSherlockPermission, shell=True, text=True)
            doChangeSherlockPermission.wait()

            if doChangeSherlockPermission.returncode == 0:
                print(Fore.YELLOW + f'Succeeded in changing Sherlock ownership to {newUser} at\n{thisTime}\nPlease proceed to {path}Sherlock/install.sh for installation :)...\n')
            else:
                print(Fore.RED + f'Failed to change Sherlock ownership to {newUser}...\nSkipping...\n')

        else:
            print(Fore.RED + "\nFailed to download sherlock...\nSkipping...\n")

        # Installing RedHawk
        print(Fore.YELLOW + "\nDownloading RedHawk...\n")
        installRedHawk = f'echo {sudo_password} | sudo git clone https://github.com/Tuhinshubhra/RED_HAWK.git'
        doInstallRedHawk = subprocess.Popen(installRedHawk, shell=True, text=True)
        doInstallRedHawk.wait()

        if doInstallRedHawk.returncode == 0:
            print(Fore.YELLOW + "\nInstallation of RedHawk has succeeded!\nProceeding to change permissions...\n")
            changeRedHawkPermissions = f'echo {sudo_password} | sudo chown {newUser} {path}RED_HAWK; echo {sudo_password} | sudo chmod 777 {newUser} {path}RED_HAWK;'
            doChangeRedHawkPermissions = subprocess.Popen(changeRedHawkPermissions, shell=True, text=True)
            if doChangeRedHawkPermissions.returncode == 0:
                print(Fore.YELLOW + f'Succeeded in changing RED_HAWK ownership & permissions!\n')
            else:
                print(Fore.RED + f'Failed to change ownership & permissions for RED_HAWK...\nSkipping...\n')
        else:
            print(Fore.RED + "\nFailed to install RedHawk...\n")                    

        # Installing hping3
        print(Fore.YELLOW + "\nInstalling hping3...\n")
        installHping3 = f'echo {sudo_password} | sudo apt install hping3 -y'
        doInstallHping3 = subprocess.Popen(installHping3, shell=True, text=True)
        doInstallHping3.wait()
                    
        if doInstallHping3.returncode == 0:
            print(Fore.YELLOW + f'Succeeded in installing of hping3 at\n{thisTime}!\n')
        else:
            print(Fore.RED + f'\nFailed to install hping3 at\n{thisTime}\n')

        # Installing Apache2
        print(Fore.YELLOW + f'\nInstalling Apache2...\n')
        installApache2 = f'echo {sudo_password} | sudo apt install apache2 -y'
        doInstallApache2 = subprocess.Popen(installApache2, shell=True, text=True)
        doInstallApache2.wait()

        if doInstallApache2.returncode == 0:
            print(Fore.YELLOW + f'\nSucceeded in installing Apache2 at\n{thisTime}\n')
        else:
            print(Fore.RED + f'\nFailed to install Apache2 at\n{thisTime}\n')

        # Installing SecLists
        print(Fore.YELLOW + "\nInstalling Seclist...\n")
        installSeclist = f'cd {path} && echo {sudo_password} | sudo git clone https://github.com/danielmiessler/SecLists.git'
        doInstallSeclist = subprocess.Popen(installSeclist, shell=True, text=True)
        doInstallSeclist.wait()

        if doInstallSeclist.returncode == 0:
            print(Fore.YELLOW + f'\nInstallation of Seclist has succeeded at\n{thisTime}\n')
        else:
            print(Fore.RED + f'\nFailed to install Seclist at\n{thisTime}\n')


        # Installing VSCode
        print(Fore.YELLOW + f'\nInstalling VSCode...\n')
        installVscode1 = f'echo {sudo_password} | sudo apt install apt-transport-https -y'
        doInstallVscode1 = subprocess.Popen(installVscode1, shell=True, text=True)
        doInstallVscode1.wait()
        vscodeDir1 = f'echo {sudo_password} | sudo mkdir /etc/apt/sources.list.d/vscode.list'

        if doInstallVscode1.returncode == 0:
            print(Fore.YELLOW + "\nInstallation of apt-transport-https has succeeded!\nContinuing to add Microsoft package keys!\n")
            installVscode2 = f'echo {sudo_password} | curl https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > packages.microsoft.gpg'
            doInstallVscode2 = subprocess.Popen(installVscode2, shell=True, text=True)
            doInstallVscode2.wait()
                
            if doInstallVscode2.returncode == 0:
                print(Fore.YELLOW + "\nInstallation of Microsoft package KEYS has succeeded!\nContinuing to install Microsoft packages\n")
                installVscode3 = f'echo {sudo_password} | sudo install -o root -g root -m 644 packages.microsoft.gpg /usr/share/keyrings/'
                doInstallVscode3 = subprocess.Popen(installVscode3, shell=True, text=True)
                doInstallVscode3.wait()
                    
                if doInstallVscode3.returncode == 0:
                    print(Fore.YELLOW + f'\nSucceeded in installing Microsoft packages at\n{thisTime}\n')
                    installVscode4 = f'echo {sudo_password} | sudo echo "deb [arch=amd64 signed-by=/usr/share/keyrings/packages.microsoft.gpg] https://packages.microsoft.com/repos/vscode stable main" >> /etc/apt/sources.list.d/vscode.list'
                    doInstallVscode4 = subprocess.Popen(installVscode4, shell=True, text=True)
                    doInstallVscode4.wait()
                        
                    if doInstallVscode4.returncode == 0:
                        print(Fore.YELLOW + f'Succeeded in installing VSCode pre-requisites at\n{thisTime}\n')
                        print(Fore.YELLOW + "\nUpdating && Installing VSCode!\n")
                        installVscode5 = f'echo {sudo_password} | sudo apt install code -y'
                        doInstallVscode5 = subprocess.Popen(installVscode5, shell=True, text=True)
                        if doInstallVscode5.returncode == 0:
                            print(Fore.YELLOW + f'Succeeded in installing VSCode at\n{thisTime}\n')
                        else:
                            print(Fore.RED + f'\nFailed to install VSCode...\nSkipping...\n')
                    else:
                        print(Fore.RED + f'Failed to install VSCode pre-requisites at\n{thisTime}')

                else:
                    print(Fore.RED + "\nFailed to install Microsoft packages...\nSkipping VScode...\n")
            else:
                print(Fore.RED + "\nFailed to install Microsoft package KEYS...\nSkipping VScode...\n")
        else:
            print(Fore.RED + f'\nInstallation of apt-transport-https has failed...\nSkipping to install VScode...\n')
                
        # Install Guake
        print(Fore.WHITE + "### Installing Guake ###")
        installGuake = f'echo {sudo_password} | sudo apt install guake -y'
        doInstallGuake = subprocess.Popen(installGuake, shell=True, text=True)
        doInstallGuake.wait()
                    
        if doInstallGuake.returncode == 0:
            print(Fore.YELLOW + f'Succeeded in installing Guake at\n{thisTime}')
        else:
            print(Fore.RED + f'Failed to install Guake...\nSkipping...\n')
           

        # Install tmux
        print(Fore.YELLOW + "\nInstalling TMUX...\n")
        print(Style.RESET_ALL)
        installTmux = f'echo {sudo_password} | sudo apt install tmux -y'
        doInstallTmux = subprocess.Popen(installTmux, shell=True, text=True)
        doInstallTmux.wait()

        if doInstallTmux.returncode == 0:
            print(Fore.YELLOW + f'Succeeded in installing TMUX at\n{thisTime}')
        else:
            print(Fore.RED + f'Failed to install TMUX...\nSkipping...\n')
                    
        # Install NFS
        print(Fore.YELLOW + "####################################")
        print(Fore.YELLOW + "### Installing nfs-kernel-server ###")
        print(Fore.YELLOW + "####################################")
        print(Style.RESET_ALL)
        installNfs = f'echo {sudo_password} | sudo apt install nfs-kernel-server -y'
        doInstallNfs = subprocess.Popen(installNfs, shell=True, text=True)
        doInstallNfs.wait()
        if doInstallNfs.returncode == 0:
            print(Fore.YELLOW + f'\nSucceeded in installing NFSat\n{thisTime}')
        else:
            print(Fore.RED + f'\nFailed to install NFS at\n{thisTime}\nSkipping...\n')

        # Install xsser
        print(Fore.YELLOW + "### Installing xsser ###")
        print(Style.RESET_ALL)
        installXsser = f'echo {sudo_password} | sudo apt install xsser -y'
        doInstallXsser = subprocess.Popen(installXsser, shell=True, text=True)
        doInstallXsser.wait()

        if doInstallXsser.returncode == 0:
            print(Fore.YELLOW + f'Succeeded in installing XSSER at\n{thisTime}\n')
        else:
            print(Fore.RED + f'Failed to install XSSER at\n{thisTime}\nSkipping...\n')
            
        # Install EyeWitness
        print(Fore.YELLOW + "### Installing EyeWitness ###")
        print(Style.RESET_ALL)
        installEyewitness = f'cd {path} && echo {sudo_password} | sudo git clone https://github.com/RedSiege/EyeWitness.git'
        doInstallEyewitness = subprocess.Popen(installEyewitness, shell=True, text=True)
        doInstallEyewitness.wait()

        if doInstallEyewitness.returncode == 0:
            print(Fore.YELLOW + f'Succeeded in downloading EyeWitness at\n{thisTime}\n')
            changeEyeWitnessPermission = f'echo {sudo_password} | sudo chown {newUser} {path}EyeWitness; echo {sudo_password} | sudo chmod 777 {path}EyeWitness;'
            doChangeEyeWitnessPermission = subprocess.Popen(changeEyeWitnessPermission, shell=True, text=True)
            doChangeEyeWitnessPermission.wait()
            if doChangeEyeWitnessPermission.returncode == 0:
                print(Fore.YELLOW + f'Succeeded in changing permission for {path}EyeWitness at\n{thisTime}\n')
            else:
                print(Fore.RED + f'Failed to change permissions for {path}EyeWitness at\n{thisTime}\nSkipping...\n')

        # Install Evil-WinRM
        print(Fore.YELLOW + "### Installing Evil-WinRM ###")
        print(Style.RESET_ALL)
        installEvilwinrm = f'echo {sudo_password} | sudo git clone https://github.com/Hackplayers/evil-winrm.git'
        doInstallEvilwinrm = subprocess.Popen(installEvilwinrm, shell=True, text=True)
        doInstallEvilwinrm.wait()

        if doInstallEvilwinrm.returncode == 0:
            print(Fore.YELLOW + f'Succeeded in downloading Evil-WinRM at {path}\nProceeding to change permissions for {path}EyeWitness\n')
            changeEvilWinRm = f'echo {sudo_password} | sudo chown {newUser} {path}evil-winrm; echo {sudo_password} | sudo chmod 777 {path}evil-winrm;'
        else:
            print(Fore.RED + f'Failed to download Evil-WinRM at {path} at\n{thisTime}...\nSkipping...\n')

                    
        # Install Powerline
        print(Fore.YELLOW + "### Installing Powerline ###")
        print(Style.RESET_ALL)
        installPowerline = f'cd {path} && echo {sudo_password} | sudo git clone https://github.com/powerline/powerline.git'
        doInstallPowerline = subprocess.Popen(installPowerline, shell=True, text=True)
        doInstallPowerline.wait()

        if doInstallPowerline.returncode == 0:
            print(Fore.YELLOW + f'Succeeded in downloading Powerline at {path} at\n{thisTime}\n')
            changePowerLine = f'echo {sudo_password} | sudo chown {newUser} {path}powerline; echo {sudo_password} | sudo chmod 777 {path}powerline'
            doChangePowerLine = subprocess.Popen(changePowerLine, shell=True, text=True)
            doChangePowerLine.wait()
        else:
            print(Fore.RED + f'Failed to download Powerline at\n{thisTime}...\nSkipping...\n')
                    
        # Install Remote System Logging rsyslog
        print(Fore.YELLOW + "### Installing rsyslog ###")
        print(Style.RESET_ALL)
        installRsyslog = f'echo {sudo_password} | sudo apt install rsyslog -y'
        doInstallRsyslog = subprocess.Popen(installRsyslog, shell=True, text=True)
        doInstallRsyslog.wait()

        if doInstallRsyslog.returncode == 0:
            print(Fore.YELLOW + f'Succeeded in installing Remote System Logging at {thisTime}\n')
            print(Fore.YELLOW + f'Enabling rsyslog service at {thisTime}...\n')
            enableRsyslog = f'echo {sudo_password} | sudo systemctl enable rsyslog'
            doEnableRsyslog = subprocess.Popen(enableRsyslog, shell=True, text=True)
            doEnableRsyslog.wait()
                        
            if doEnableRsyslog.returncode == 0:
                print(Fore.YELLOW + f'Succeeded in enabling rsyslog at\n{thisTime}\nStarting up rsyslog!\n')
                startRsyslog = f'echo {sudo_password} | sudo systemctl start rsyslog'
                doStartRsyslog = subprocess.Popen(startRsyslog, shell=True, text=True)
                doStartRsyslog.wait()
                if doStartRsyslog.returncode == 0:
                    print(Fore.YELLOW + f'\nSucceeded in starting up rsyslog at\n{thisTime}\n')
                else:
                    print(Fore.RED + f'Failed to start rsyslog at\n{thisTime}...\n')
            else:
                print(Fore.RED + f'\nFailed to enable rsyslog at\n{thisTime}\n')
        else:
            print(Fore.RED + f'Failed to install Remote System Logging (rsyslog) at\n{thisTime}\nSkipping...\n')

        # Install Linux Containers
        print(Fore.YELLOW + "#########################################")
        print(Fore.YELLOW + "### Installing Linux Containers (LXC) ###")
        print(Fore.YELLOW + "#########################################")
        print(Style.RESET_ALL)
            
        installLXC = f'echo {sudo_password} | sudo apt install lxc -y'
        doInstallLXC = subprocess.Popen(installLXC, shell=True, text=True)
        doInstallLXC.wait()

        if doInstallLXC.returncode == 0:
            print(Fore.YELLOW + f'Succeeded in installing LXC at\n{thisTime}\nContinuing to install Bridge Utilities (brtctl)\n')
            # Install Bridge Utilities to allow Linux Containers & Docker containers
            print(Fore.YELLOW + "###############################")
            print(Fore.YELLOW + "### Installing bridge-utils ###")
            print(Fore.YELLOW + "###############################")
            print(Fore.YELLOW + "######################\n### To talk to Container Host ###\n# Usage #\n# brctl show = Show existing bridges #\n# sudo brctl addbr <lxcbr0> = Add a bridge interface named lxcbr0 #\n# sudo brctl delbr <lxcbr0> = Remove a bridge interface named lxcbr0 #\n# sudo brctl addif lxcbr0 eth0 = Add eth0 to bridge interface lxcbr0 #\n# sudo brctl delif lxcbr0 eth0 = Remove eth0 from lxcbr0 #\n")
            # Usage 
            # brctl show = Show existing bridges
            # sudo brctl addbr <lxcbr0> = Add a bridge interface named 'lxcbr0'
            # sudo brctl delbr <lxcbr0> = Remove a bridge interface named 'lxcbr0'
            # sudo brctl addif lxcbr0 eth0 = Add eth0 to bridge interface 'lxcbr0'
            # sudo brctl delif lxcbr0 eth0 = Remove eth0 from lxcbr0
            # 
            print(Style.RESET_ALL)
            #os.system('sudo -u {} sudo apt install bridge-utils -y'.format(newUser))
            installBrctl = f'echo {sudo_password} | sudo apt install bridge-utils -y'
            doInstallBrctl = subprocess.Popen(installBrctl, shell=True, text=True)
            doInstallBrctl.wait()

            if doInstallBrctl.returncode == 0:
                print(Fore.YELLOW + f'Succeeded in installing Bridge Utilities (brctl) at\n{thisTime}\n')
            else:
                print(Fore.RED + f'Failed to install Bridge Utilities (brctl) at\n{thisTime}\nSkipping...\n')
        else:
            print(Fore.RED + f'Failed to install LXC at\n{thisTime}\nSkipping...\n')

        print(Fore.YELLOW + "#########################################")
        print(Fore.YELLOW + "### Installing Linux Containers (LXD) ###")
        print(Fore.YELLOW + "#########################################")
        print(Style.RESET_ALL)
        #os.system('sudo -u {} sudo /usr/bin/snap install lxd'.format(newUser))
        #os.system('sudo -u {} sudo apt install lxc -y'.format(newUser))
        installSNAP = f'echo {sudo_password} | sudo apt install snapd -y'
        doInstallSNAP = subprocess.Popen(installSNAP, shell=True, text=True)
        doInstallSNAP.wait()

        if doInstallSNAP.returncode == 0:
            print(Fore.YELLOW + f'Succeeded in installing SNAP at\n{thisTime}\nEnabling SNAPD...\n')
            enableSNAP = f'echo {sudo_password} | sudo systemctl enable snapd'
            doEnableSNAP = subprocess.Popen(enableSNAP, shell=True, text=True)
            doEnableSNAP.wait()
            if doEnableSNAP.returncode == 0:
                print(Fore.YELLOW + f'Succeede in Enabling SNAPD at\n{thisTime}\nStarting up SNAPD!\n')
                startSNAP = f'echo {sudo_password} | sudo systemctl start snapd'
                doStartSNAP = subprocess.Popen(startSNAP, shell=True, text=True)
                doStartSNAP.wait()
                if doStartSNAP.returncode == 0:
                    print(Fore.YELLOW + f'Succeeded in starting up SNAPD at\n{thisTime}\nInstalling LXD using SNAP!\n')
                    installLXD = f'echo {sudo_password} | sudo /usr/bin/snap install lxd'
                    doInstallLXD = subprocess.Popen(installLXD, shell=True, text=True)
                    doInstallLXD.wait()
                    if doInstallLXD.returncode == 0:
                        print(Fore.YELLOW + f'Succeeded in installing LXD at\n{thisTime}\n')
                    else:
                        print(Fore.RED + f'Failed to install LXD at\n{thisTime}\n')
                else:
                    print(Fore.YELLOW + f'Failed to start SNAPD\nSkipping to install LXD...\n')
            else:
                print(Fore.RED + f'Failed to Enable SNAPD...\nSkipping to install LXD...\n')
        else:
            print(Fore.RED + f'Failed to install SNAP...\nSkipping to install LXD...\n')

        # Install Docker
        print(Fore.YELLOW + "### Installing Docker ###")
        print(Style.RESET_ALL)
        #os.system('sudo -u {} sudo apt install docker\.io -y'.format(newUser))
        installDocker = f'echo {sudo_password} | sudo apt install docker\.io -y'
        doInstallDocker = subprocess.Popen(installDocker, shell=True, text=True)
        doInstallDocker.wait()

        if doInstallDocker.returncode == 0:
            print(Fore.YELLOW + f'Succeeded in installing Docker at\n{thisTime}\n')
        else:
            print(Fore.RED + f'Failed to install Docker at\n{thisTime}\nSkipping...\n')

        # Install BeefProject
        print(Fore.YELLOW + "### Installing Beef-XSS ###")
        print(Style.RESET_ALL)
        #os.system('sudo -u {} sudo apt install beef-xss -y'.format(newUser))
        beefXSSPath = f'/home/{newUser}/Desktop/tools/beef-xss/'
        installBeefXSS = f'echo {sudo_password} | sudo apt install beef-xss -y'
        doInstallBeefXSS = subprocess.Popen(installBeefXSS, shell=True, text=True)
        doInstallBeefXSS.wait()

        if doInstallBeefXSS.returncode == 0:
            print(Fore.YELLOW + f'Succeeded in installing Beef-XSS at\n{thisTime}\n')
            print(Fore.YELLOW + f'\nEnabling Beef-XSS binary at\n{thisTime}...\n')
            enableBeefXSS = f'echo {sudo_password} | sudo systemctl enable beef-xss'
            doEnableBeefXSS = subprocess.Popen(enableBeefXSS, shell=True, text=True)
            doEnableBeefXSS.wait()
                
            if doEnableBeefXSS.returncode == 0:
                print(Fore.YELLOW + f'Succeeded in enabling Beef-XSS\nStarting up Beef-XSS!\n')
                startBeefXSS = f'echo {sudo_password} | sudo systemctl start beef-xss'
                doStartBeefXSS = subprocess.Popen(startBeefXSS, shell=True, text=True)
                doStartBeefXSS.wait()
                    
                if doStartBeefXSS.returncode == 0:
                    print(Fore.YELLOW + f'Succeeded in starting up Beef-XSS at\n{thisTime}\nProceeding to configure Beef-XSS!\n')
                    # Locate Beef-XSS config file
                    # Save it to var $beefDir
                                
                    print(Fore.YELLOW + f'\nChanging Beef-XSS login credentials...\n')
                    #beefnewUser = input(Fore.YELLOW + "Enter new newUsername for Beef-XSS UI login: ")
                    beefPasswd = getpass.getpass('Enter new Beef-XSS password: ')
                    editLoginCommand = f'echo {sudo_password} | sudo sed -i \'s/newUser\: beef/newUser\: {newUser}/g\' /etc/beef-xss/config.yaml; echo {sudo_password} | sudo sed -i \'s/passwd\: beef/passwd\: {newPassword}/g\' /etc/beef-xss/config.yaml'
                    doEditLogin=subprocess.Popen(editLoginCommand, text=True, shell=True)
                    doEditLogin.wait()
                        
                    if doEditLogin.returncode == 0:
                        print(Fore.YELLOW + f'\nSucceeded in changing Beef-XSS Login credentials in /etc/beef-xss/config.yaml at\n{thisTime}\n\n')
                        ### Creating a directory to store current Beef-XSS Login credentials
                        print(Fore.YELLOW + f'\nCreating a directory:\n{beefXSSPath}\nTo store current Beef-XSS Login credentials\n')
                        createLoginCommand = f'echo {sudo_password} | sudo mkdir {beefXSSPath}'
                        doCreateLogin=subprocess.Popen(createLoginCommand, text=True, shell=True)
                        doCreateLogin.wait()
                            
                        if doCreateLogin.returncode == 0:
                            print(Fore.YELLOW + f'\nSucceeded in creating a directory for Beef-XSS Login credentials file at\n{thisTime}\n')
                            print(Fore.YELLOW + f'\nPurging existing login.txt in {beefXSSPath}login.txt\n')
                            purgeLoginTxt = f'echo {sudo_password} | sudo rm -rf {beefXSSPath}login.txt;'
                            doPurgeLoginTxt=subprocess.Popen(purgeLoginTxt, text=True, shell=True)
                            doPurgeLoginTxt.wait()
                            if doPurgeLoginTxt.returncode == 0:
                                print(Fore.YELLOW + f'\nSucceeded in purging existing Login credentials file in {beefXSSPath} at\n{thisTime}\n')
                            else:
                                print(Fore.YELLOW + f'\nFailed to purge existing Login credentials in {beefXSSPath}\nSkipping...\n')
                            ###
                            print(Fore.YELLOW + f'\nCreating login.txt in {beefXSSPath}login.txt at\n{thisTime}\n')
                            createLoginTxt = f'echo {sudo_password} | sudo touch {beefXSSPath}login.txt; echo {sudo_password} | sudo chmod 400 {beefXSSPath}login.txt; echo {sudo_password} | sudo chown {newUser} {beefXSSPath}login.txt;'
                            doCreateLoginTxt = subprocess.Popen(createLoginTxt, text=True, shell=True)
                            doCreateLoginTxt.wait()
                                
                            if doCreateLoginTxt.returncode == 0:
                                print(Fore.YELLOW + f'\nSucceeded in creating Login credentials in {beefXSSPath}login.txt at\n{thisTime}\n')
                                ###
                                # Verifying Beef-XSS login credentials changes
                                print(Fore.YELLOW + f'\nSaving the current Beef-XSS login credentials...\n')
                                saveLogin = f'newUser=$(echo {sudo_password} | sudo egrep "\s+{newUser}\:\s+(.*)" /etc/beef-xss/config.yaml); passwd=$(echo {sudo_password} | sudo egrep "\s+passwd\:\s+(.*)" /etc/beef-xss/config.yaml); echo {sudo_password} | sudo echo $newUser > {beefXSSPath}login.txt; echo {sudo_password} | sudo echo $passwd >> {beefXSSPath}login.txt;'
                                doSaveLogin = subprocess.Popen(saveLogin, text=True, shell=True)
                                doSaveLogin.wait()
                                    
                                if doSaveLogin.returncode == 0:
                                    print(Fore.YELLOW + f'\nSucceeded in saving current Beef-XSS Login credentials at\n{thisTime}\nPlease cat {beefXSSPath}login.txt for your login credentials :)\n')
                                    # Restart Beef-XSS
                                    print(Fore.YELLOW + f'\nRestarting Beef-XSS...\n')
                                    restartBeefXSS = f'echo {sudo_password} | sudo systemctl restart beef-xss'
                                    doRestartBeefXSS = subprocess.Popen(restartBeefXSS, shell=True, text=True)
                                    doRestartBeefXSS.wait()
                                        
                                    if doRestartBeefXSS.returncode == 0:
                                        print(Fore.YELLOW + f'\nSucceeded in restarting Beef-XSS at\n{thisTime}\n')
                                        #os.system('sudo systemctl restart beef-xss')
                                        print(Fore.YELLOW + f'\n\nBeef-XSS is now accessible at http://127.0.0.1:3000/ui/authentication\n')
                                    else:
                                        print(Fore.RED + f'\nFailed to restart Beef-XSS...\nYou may restart Beef-XSS yourself then to login using your credentials in {beefXSSPath}login.txt\nat http://127.0.0.1:3000/ui/authentication\nSkipping...\n')
                                        ###
                                        ###
                                else:
                                    print(Fore.RED + f'Failed to save current Beef-XSS Login credentials in {beefXSSPath} at\n{thisTime}\nSkipping...\n')
                            else:
                                print(Fore.RED + f'\nFailed to create a new login credentials in {beefXSSPath}login.txt at\n{thisTime}\n\nYou may change your Beef-XSS login credentials in /etc/beef-xss/config.yaml manually...\nSkipping...\n')
                        else:
                            print(Fore.RED + f'\nFailed to create a file as {beefXSSPath}login.txt for saving your current Beef-XSS Login credentials at\n{thisTime}\n\nSkipping...\n')
                    else:
                        print(Fore.RED + f'\nFailed to change Beef-XSS Login credentials file in /etc/beef-xss/config.yaml at\n{thisTime}\n\nYou may change it manually in /etc/beef-xss/config.yaml\n\n')
                else:
                    print(Fore.RED + f'\nFailed to start Beef-XSS using systemctl at\n{thisTime}\n\nYou may manually start Beef-XSS by:\nsudo systemctl start beef-xss\n\n')
            else:
                print(Fore.RED + f'\nFailed to enable Beef-XSS by:\nsudo systemctl enable beef-xss\nat\n{thisTime}\nSkipping...\n')
        else: 
            print(Fore.RED + f'\nFailed to apt install beef-XSS -y at\n{thisTime}\nSkipping...\n')
            
                  
        # Install OpenVAS
        print(Fore.WHITE + f'********************************************')
        print(Fore.WHITE + f'************Installing OpenVAS**************')
        print(Fore.WHITE + f'This can take up to 2 hours to complete installation...')
        print(Fore.WHITE + f'********************************************')
        print(Fore.WHITE + f'********************************************')

        #os.system('sudo apt install openvas -y')
        installOpenVAS = f'echo {sudo_password} | apt install openvas -y'
        doInstallOpenVAS = subprocess.Popen(installOpenVAS, shell=True, text=True)
        doInstallOpenVAS.wait()

        if doInstallOpenVAS.returncode == 0:
            print(Fore.YELLOW + f'\nSucceeded in installing OpenVAS at\n{thisTime}\nContinuing to gvm-setup...\n')
            gvmSetup = f'echo {sudo_password} | sudo gvm-setup'
            doGvmSetup = subprocess.Popen(gvmSetup, shell=True, text=True)
            doGvmSetup.wait()
                
            if doGvmSetup.returncode == 0:
                print(Fore.YELLOW + f'\nSucceeded in setting up GVM at\n{thisTime}\n')
            else:
                print(Fore.RED + f'\Failed to set up ngvm-setup :( at\n{thisTime}\n')
        else:
            print(Fore.RED + f'\nFailed to install OpenVAS...\nat:\n{thisTime}\nCheck whether you\'ve run PostgreSQL 15 && 14 PORTs update...\nFailed to swap PostgreSQL15 TCP port (e.g. 5432) AND PostgreSQL14 TCP ports (e.g. 5433) will induce this kind of error...\n')

        print(Fore.WHITE + f'\n\nAll open-source tools are installed!!\nProceeding to clean up phase!\n')
