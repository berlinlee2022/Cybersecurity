# --------------
# Imports modules
# --------------
import os
from colorama import Fore, Back, Style
import subprocess
import getpass
import time

def installTools():

    install = input(Fore.WHITE + '[x] Do you wanna install custom tools? [x] (y/N): ')

    if install.lower() == "y":
        # Default Tools
        print(Fore.YELLOW + "### Installing Default Tools ###")
        user = input(Fore.WHITE + '\nPlease enter the user to run this script: ')
        sudo_password = getpass.getpass('\nEnter your sudo password: ')
        print(Style.RESET_ALL)

        # Create directory 'tools'
        print(Fore.YELLOW + "***********************************")
        print(Fore.YELLOW + "Creating /home/{user}/Desktop/tools")
        print(Fore.YELLOW + "***********************************")
        print(Style.RESET_ALL)
        createToolDir1 = f'echo {sudo_password} | sudo mkdir /home/{user}/Desktop'
        doCreateToolDir1 = subprocess.Popen(createToolDir1, shell=True, text=True)
        doCreateToolDir1.wait()
        createToolDir2 = f'echo {sudo_password} | sudo mkdir /home/{user}/Desktop/tools'
        doCreateToolDir2 = subprocess.Popen(createToolDir2, shell=True, text=True)
        doCreateToolDir2.wait()
        change = f'echo {sudo_password} | sudo chmod 777 /home/{user}; echo {sudo_password} | sudo chmod 777 /home/{user}/Desktop; echo {sudo_password} | sudo chmod 777 /home/{user}/Desktop/tools; echo {sudo_password} | sudo chown {user} /home/{user}; echo {sudo_password} | sudo chown {user} /home/{user}/Desktop; echo {sudo_password} | sudo chown {user} /home/{user}/Desktop/tools;'
        doChange = subprocess.Popen(change, shell=True, text=True)
        doChange.wait()
        #os.system('sudo mkdir /home/phoenix/Desktop/tools')

        if 0 == 0:
            print(Fore.YELLOW + "\nThe following directory has been created successfully!\n/home/{user}/Desktop/tools\n")
            print(Style.RESET_ALL)
            ### Package managers
            package = input(Fore.WHITE + "\n[x] Do you wanna install package managers? [x] (y/N): ")
            if package.lower() == "y":
                print(Fore.YELLOW + "*******************************")
                print(Fore.YELLOW + "\nInstalling package managers\nSNAP\nGEM\nNixNote2\nNautilus-dropbox\nKeepassxc\nPython3-pip\nDNF\n")
                installPackage = f'echo {sudo_password} | sudo apt install snapd gem nixnote2 nautilus-dropbox keepassxc python3-pip dnf -y'
                doInstallPackage = subprocess.Popen(installPackage, shell=True, text=True)
                doInstallPackage.wait()

                if doInstallPackage.returncode == 0:
                    print(Fore.YELLOW + "\nInstallation of package managers has succeeded!\n")
                else:
                    print(Fore.RED + "\nInstallation of package managers has failed...:(\n")
            else:
                print(Fore.YELLOW + "\nNot installing package managers...\nSkipping...\n")

            ### Recon tools
            recon = input(Fore.WHITE + '\n[x] Do you wanna install Recon tools? [x] (y/N): ')
            if recon.lower() == "y":
                print(Fore.YELLOW + "\n### Installing recon tools...###\n")
                # Installing Sn1per
                sniper = input(Fore.WHITE + "[x] Do you wanna install Sn1per? [x] (y/N): ")
                if sniper.lower() == "y":
                    print(Fore.YELLOW + "\nInstalling Sn1per...\n")
                    installSn1per = f'cd /home/{user}/Desktop/tools; echo {sudo_password} | sudo git clone https://github.com/1N3/Sn1per.git; echo {sudo_password} | sudo chmod 777 /home/phoenix/Desktop/tools/Sn1per/install.sh' 
                    doInstallSn1per = subprocess.Popen(installSn1per, shell=True, text=True)
                    doInstallSn1per.wait()

                    if doInstallSn1per.returncode == 0:
                        print(Fore.YELLOW + "\nSn1per has been installed successfully!\n")
                    else:
                        print(Fore.RED + "\nSn1per has NOT been installed successfully...:(\n")
                else:
                    print(Fore.YELLOW + "\nNot installing Sn1per...\nSkipping...\n")

                # Installing pyautogui
                pyautogui = input(Fore.WHITE + "[x] Do you wanna install pyautogui? [x] (y/N): ")    
                if pyautogui.lower() == "y":
                    print(Fore.YELLOW + "\nInstalling pyautogui...\n")
                    installPyautogui = f'pip3 install pyautogui'
                    doInstallPyautogui = subprocess.Popen(installPyautogui, shell=True, text=True)
                    doInstallPyautogui.wait()

                    if doInstallPyautogui.returncode == 0:
                        print(Fore.YELLOW + "\nInstallation of pyautogui has succeeded!\n")
                    else:
                        print(Fore.RED + "\nFailed to install pyautogui...:(\n")
                else:
                    print(Fore.YELLOW + "\nNot installing pyautogui...\nSkipping...\n")

                # Installing Sherlock
                sherlock = input(Fore.WHITE + '[x] Do you wanna install Sherlock? [x] (y/N): ')
                if sherlock.lower() == "y":
                    print(Fore.YELLOW + "\nInstalling Sherlock...\n")
                    installSherlock = f'cd /home/{user}/Desktop/tools; echo {sudo_password} | sudo git clone https://github.com/sherlock-project/sherlock.git'
                    doInstallSherlock = subprocess.Popen(installSherlock, shell=True, text=True)
                    doInstallSherlock.wait()

                    if doInstallSherlock.returncode == 0:
                        print(Fore.YELLOW + "\nInstallation of Sherlock has succeeded!\n")

                    else:
                        print(Fore.RED + "\nInstallation of Sherlock has failed...\n")
                else:
                    print(Fore.YELLOW + "\nNot installing Sherlock...\nSkipping...\n")

                # Installing RedHawk
                redhawk = input(Fore.WHITE + "[x] Do you wanna install RedHawk? [x] (y/N): ")
                if redhawk.lower() == "y":
                    print(Fore.YELLOW + "\nInstalling RedHawk...\n")
                    installRedHawk = f'cd /home/{user}/Desktop/tools; echo {sudo_password} | sudo git clone https://github.com/Tuhinshubhra/RED_HAWK.git'
                    doInstallRedHawk = subprocess.Popen(installRedHawk, shell=True, text=True)
                    doInstallRedHawk.wait()

                    if doInstallRedHawk.returncode == 0:
                        print(Fore.YELLOW + "\nInstallation of RedHawk has succeeded!\n")
                    else:
                        print(Fore.RED + "\nFailed to install RedHawk...\n")
                    
                else:
                    print(Fore.YELLOW + "\nNot installing RedHawk...\nSkipping...\n")

                # Installing hping3
                hping3 = input(Fore.WHITE + "[x] Do you wanna install hping3? [x] (y/N): ")
                if hping3.lower() == "y":
                    print(Fore.YELLOW + "\nInstalling hping3...\n")
                    installHping3 = f'echo {sudo_password} | sudo apt install hping3 -y'
                    doInstallHping3 = subprocess.Popen(installHping3, shell=True, text=True)
                    doInstallHping3.wait()
                    
                    if doInstallHping3.returncode == 0:
                        print(Fore.YELLOW + "\nInstallation of hping3 has succeeded!\n")
                    else:
                        print(Fore.RED + "\nFailed to install hping3...\n")
                else:
                    print(Fore.YELLOW + "\nNot installing hping3...\nSkipping...\n")
            else:
                print(Fore.YELLOW + "\nNot installing recon tools...\nSkipping...\n")

            ### Optional tools
            print(Fore.WHITE + "*************************")
            print(Fore.WHITE + "Installing optional tools")
            print(Fore.WHITE + "*************************")
            option = input(Fore.WHITE + "\n[x] Do you wanna install optional tools? [x] (y/N): ")
            if option.lower() == "y":
                # Installing Apache2
                apache2 = input(Fore.WHITE+ "\n[x] Do you wanna install apache2? [x] (y/N): ")
                if apache2.lower() == "y":
                    print(Fore.YELLOW + "\nInstalling Apache2...\n")
                    installApache2 = f'echo {sudo_password} | sudo apt install apache2 -y'
                    doInstallApache2 = subprocess.Popen(installApache2, shell=True, text=True)
                    doInstallApache2.wait()

                    if doInstallApache2.returncode == 0:
                        print(Fore.YELLOW + "\nInstallation of Apache2 has succeeded!\n")
                    else:
                        print(Fore.RED + "\nFailed to install Apache2...\n")
                else:
                    print(Fore.YELLOW + "\nNot installing Apache2...\nSkipping...\n")

                # Installing SecLists
                seclist = input(Fore.WHITE + "\n[x] Do you wanna install SecList? [x] (y/N): ")
                if seclist.lower() == "y":
                    print(Fore.YELLOW + "\nInstalling Seclist...\n")
                    installSeclist = f'echo {sudo_password} | sudo git clone https://github.com/danielmiessler/SecLists.git /opt/'
                    doInstallSeclist = subprocess.Popen(installSeclist, shell=True, text=True)
                    doInstallSeclist.wait()

                    if doInstallSeclist.returncode == 0:
                        print(Fore.YELLOW + "\nInstallation of Seclist has succeeded!\n")
                    else:
                        print(Fore.RED + "\nFailed to install Seclist...\n")
                else:
                    print(Fore.YELLOW + "\nNot installing Seclist...\nSkipping...\n")

                # Installing VSCode
                vscode = input(Fore.WHITE + "[x] Do you wanna install VSCode [x]? (y/N): ")
                if vscode.lower() == "y":
                    print(Fore.YELLOW + "\nInstalling VSCode...\n")
                    installVscode1 = f'echo {sudo_password} | sudo apt install apt-transport-https -y'
                    doInstallVscode1 = subprocess.Popen(installVscode1, shell=True, text=True)
                    doInstallVscode1.wait()

                    if doInstallVscode1.returncode == 0:
                        print(Fore.YELLOW + "\nInstallation of apt-transport-https has succeeded!\nContinuing to add Microsoft package keys!\n")
                        installVscode2 = f'echo {sudo_password} | curl https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > packages.microsoft.gpg'
                        doInstallVscode2 = subprocess.Popen(installVscode2, shell=True, text=True)
                        doInstallVscode2.wait()
                        if doInstallVscode2.returncode == 0:
                            print(Fore.YELLOW + "\nInstallation of Microsoft package KEYS has succeeded!\nContinuing to install Microsoft packages")
                            installVscode3 = f'echo {sudo_password} | sudo install -o root -g root -m 644 packages.microsoft.gpg /usr/share/keyrings/'
                            doInstallVscode3 = subprocess.Popen(installVscode3, shell=True, text=True)
                            doInstallVscode3.wait()
                            if doInstallVscode3.returncode == 0:
                                print(Fore.YELLOW + "\nInstallation of Microsoft packages has succeeded!\n")
                                installVscode4 = f'echo {sudo_password} | sudo sh -c \'echo "deb [arch=amd64 signed-by=/usr/share/keyrings/packages.microsoft.gpg] https://packages.microsoft.com/repos/vscode stable main" > /etc/apt/sources.list.d/vscode.list\''
                                doInstallVscode4 = subprocess.Popen(installVscode4, shell=True, text=True)
                                doInstallVscode4.wait()
                                if doInstallVscode4.returncode == 0:
                                    print(Fore.YELLOW + "\nInstallation of VSCode pre-requisites has succeeded!\n")
                                    print(Fore.YELLOW + "\nUpdating && Installing VSCode!\n")
                                    installVscode5 = f'echo {sudo_password} | sudo apt update; echo {sudo_password} | sudo apt install code -y'
                                    doInstallVscode5 = subprocess.Popen(installVscode5, shell=True, text=True)
                                    if doInstallVscode5.returncode == 0:
                                        print(Fore.YELLOW + "\nInstallation of VSCode has succeeded!\n")
                                    else:
                                        print(Fore.RED + "\nFailed to install VSCode...\nSkipping...\n")

                            else:
                                print(Fore.RED + "\nFailed to install Microsoft packages...\nSkipping VScode...\n")
                        else:
                            print(Fore.RED + "\nFailed to install Microsoft package KEYS...\nSkipping VScode...\n")
                    else:
                        print(Fore.RED + "\nInstallation of apt-transport-https has failed...\nSkipping to install VScode...\n")
                    #os.system('sudo -u {} sudo apt install apt-transport-https -y'.format(user))
                    #os.system('sudo -u {} curl https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > packages.microsoft.gpg'.format(user))
                    #os.system('sudo -u {} sudo install -o root -g root -m 644 packages.microsoft.gpg /usr/share/keyrings/'.format(user))
                    #os.system('sudo -u {} sudo sh -c \'echo "deb [arch=amd64 signed-by=/usr/share/keyrings/packages.microsoft.gpg] https://packages.microsoft.com/repos/vscode stable main" > /etc/apt/sources.list.d/vscode.list\''.format(user))
                    #os.system('sudo -u {} sudo apt update && sudo apt install code -y'.format(user))
                else:
                    print(Fore.WHITE + "\nNot installing VSCode...\nSkipping...\n")
                
                # Install Guake
                guake = input(Fore.WHITE + "[x] Do you wanna install Guake? [x] (y/N): ")
                if guake.lower() == "y":
                    print(Fore.WHITE + "### Installing Guake ###")
                    #os.system('sudo -u {} sudo apt install guake -y'.format(user))
                    installGuake = f'echo {sudo_password} | sudo apt install guake -y'
                    doInstallGuake = subprocess.Popen(installGuake, shell=True, text=True)
                    doInstallGuake.wait()
                    
                    if doInstallGuake.returncode == 0:
                        print(Fore.YELLOW + "\nInstallation of Guake has succeeded!\n")
                    else:
                        print(Fore.RED + "\nFailed to install Guake...\nSkipping...")
                else:
                    print(Fore.YELLOW + "\nNot installing Guake...\nSkipping...\n")               

                # Install tmux
                tmux = input(Fore.WHITE + "[x] Do you wanna install TMUX? [x] (y/N): ")
                if tmux.lower() == "y":
                    print(Fore.YELLOW + "\nInstalling TMUX...\n")
                    print(Style.RESET_ALL)
                    #os.system('sudo -u {} sudo apt install tmux -y'.format(user))
                    installTmux = f'echo {sudo_password} | sudo apt install tmux -y'
                    doInstallTmux = subprocess.Popen(installTmux, shell=True, text=True)
                    doInstallTmux.wait()

                    if doInstallTmux.returncode == 0:
                        print(Fore.YELLOW + "\nInstallation of TMUX has succeeded!\n")
                    else:
                        print(Fore.RED + "\nFailed to install TMUX...\nSkipping...\n")
                else:
                    print(Fore.WHITE + "\nNot installing TMUX...\nSkipping...\n")
                    
                # Install NFS
                nfs = input(Fore.WHITE + "[x] Do you wanna install NFS [x] (y/N): ")
                if nfs.lower() == "y":
                    print(Fore.YELLOW + "####################################")
                    print(Fore.YELLOW + "### Installing nfs-kernel-server ###")
                    print(Fore.YELLOW + "####################################")
                    print(Style.RESET_ALL)
                    #os.system('sudo -u {} sudo apt install nfs-kernel-server -y'.format(user))
                    installNfs = f'echo {sudo_password} | sudo apt install nfs-kernel-server -y'
                    doInstallNfs = subprocess.Popen(installNfs, shell=True, text=True)
                    doInstallNfs.wait()
                    if doInstallNfs.returncode == 0:
                        print(Fore.YELLOW + "\nInstallation of NFS has succeeded!\n")
                    else:
                        print(Fore.RED + "\nFailed to install NFS...\nSkipping...\n")
                else:
                    print(Fore.WHITE + "\nNot installing NFS...\nSkipping...\n")

                # Install xsser
                xsser = input(Fore.WHITE + "[x] Do you wanna install XSSER? [x] (y/N): ")
                if xsser.lower() == "y":
                    print(Fore.YELLOW + "### Installing xsser ###")
                    print(Style.RESET_ALL)
                    #os.system('sudo -u {} sudo apt install xsser -y'.format(user))
                    installXsser = f'echo {sudo_password} | sudo apt install xsser -y'
                    doInstallXsser = subprocess.Popen(installXsser, shell=True, text=True)
                    doInstallXsser.wait()

                    if doInstallXsser.returncode == 0:
                        print(Fore.YELLOW + "\nInstallation of XSSER has succeeded!\n")
                    else:
                        print(Fore.RED + "\nFailed to install XSSER...\nSkipping...\n")
                else:
                    print(Fore.WHITE + "\nNot installing XSSER...\nSkipping...\n")

                # Install EyeWitness
                eyewitness = input(Fore.WHITE + "[x] Do you wanna install EyeWitness? [x] (y/N): ")
                if eyewitness.lower() == "y":
                    print(Fore.YELLOW + "### Installing EyeWitness ###")
                    print(Style.RESET_ALL)
                    #os.system('sudo -u {} sudo git clone https://github.com/RedSiege/EyeWitness.git'.format(user))
                    installEyewitness = f'echo {sudo_password} | sudo git clone https://github.com/RedSiege/EyeWitness.git'
                    doInstallEyewitness = subprocess.Popen(installEyewitness, shell=True, text=True)
                    doInstallEyewitness.wait()

                    if doInstallEyewitness.returncode == 0:
                        print(Fore.YELLOW + "\nInstallation of EyeWitness has succeeded!\n")
                    else:
                        print(Fore.RED + "\nFailed to install EyeWitness...\nSkipping...\n")
                else:
                    print(Fore.WHITE + "\nNot installing EyeWitness...\nSkipping...\n")

                # Install Evil-WinRM
                evilwinrm = input(Fore.WHITE + "[x] Do you wanna install Evil-WinRM? [x] (y/N): ")
                if evilwinrm.lower() == "y":
                    print(Fore.YELLOW + "### Installing Evil-WinRM ###")
                    print(Style.RESET_ALL)
                    #os.system('sudo -u {} sudo git clone https://github.com/Hackplayers/evil-winrm.git'.format(user))
                    installEvilwinrm = f'echo {sudo_password} | sudo git clone https://github.com/Hackplayers/evil-winrm.git'
                    doInstallEvilwinrm = subprocess.Popen(installEvilwinrm, shell=True, text=True)
                    doInstallEvilwinrm.wait()

                    if doInstallEvilwinrm.returncode == 0:
                        print(Fore.YELLOW + "\nInstallation of Evil-WinRM has succeeded!\n")
                    else:
                        print(Fore.RED + "\nFailed to install Evil-WinRM...\nSkipping...\n")
                else:
                    print(Fore.WHITE + "\nNot installing Evil-WinRM...\nSkipping...\n")
                    
                # Install Powerline
                powerline = input(Fore.WHITE + "[x] Do you wanna install Powerline? [x] (y/N): ")
                if powerline.lower() == "y":
                    print(Fore.YELLOW + "### Installing Powerline ###")
                    print(Style.RESET_ALL)
                    #os.system('sudo -u {} sudo git clone https://github.com/powerline/powerline.git'.format(user))
                    installPowerline = f'cd /home/{user}/Desktop/tools; echo {sudo_password} | sudo git clone https://github.com/powerline/powerline.git'
                    doInstallPowerline = subprocess.Popen(installPowerline, shell=True, text=True)
                    doInstallPowerline.wait()

                    if doInstallPowerline.returncode == 0:
                        print(Fore.YELLOW + "\nInstallation of Powerline has succeeded!\n")
                    else:
                        print(Fore.RED + "\nFailed to install Powerline...\nSkipping...\n")
                else:
                    print(Fore.WHITE + "\nNot installing Powerline...\nSkipping...\n")

                # Install RPM
                rpm = input(Fore.WHITE + "[x] Do you wanna install RPM pacakage manager? [x] (y/N): ")
                if rpm.lower() == "y":
                    print(Fore.YELLOW + "### Installing RPM ###")
                    print(Style.RESET_ALL)
                    #os.system('sudo -u {} sudo apt install rpm -y'.format(user))
                    installRpm = f'echo {sudo_password} | sudo apt install rpm -y'
                    doInstallRpm = subprocess.Popen(installRpm, shell=True, text=True)
                    doInstallRpm.wait()

                    if doInstallRpm.returncode == 0:
                        print(Fore.YELLOW + "\nInstallation of RPM package manager has succeeded!\n")
                    else:
                        print(Fore.RED + "\nFailed to install RPM package manager...\nSkipping...\n")
                else:
                    print(Fore.WHITE + "\nNot installing RPM package manager...\nSkipping...\n")
                    
                # Install Remote System Logging rsyslog
                rsyslog = input(Fore.WHITE + "[x] Do you wanna install Remote System Logging (rsyslog)? [x] (y/N): ")
                if rsyslog.lower() == "y":
                    print(Fore.YELLOW + "### Installing rsyslog ###")
                    print(Style.RESET_ALL)
                    #os.system('sudo -u {} sudo apt install rsyslog -y'.format(user))
                    installRsyslog = f'echo {sudo_password} | sudo apt install rsyslog -y'
                    doInstallRsyslog = subprocess.Popen(installRsyslog, shell=True, text=True)
                    doInstallRsyslog.wait()

                    if doInstallRsyslog.returncode == 0:
                        print(Fore.YELLOW + "\nInstallation of Remote System Logging has succeeded!\n")
                        print(Fore.YELLOW + "\nEnabling rsyslog service...\n")
                        enableRsyslog = f'echo {sudo_password} | sudo systemctl enable rsyslog'
                        doEnableRsyslog = subprocess.Popen(enableRsyslog, shell=True, text=True)
                        doEnableRsyslog.wait()
                        
                        if doEnableRsyslog.returncode == 0:
                            print(Fore.YELLOW + "\nEnabling of rsyslog has succeeded!\nStarting up rsyslog!\n")
                            startRsyslog = f'echo {sudo_password} | sudo systemctl start rsyslog'
                            doStartRsyslog = subprocess.Popen(startRsyslog, shell=True, text=True)
                            doStartRsyslog.wait()
                            if doStartRsyslog.returncode == 0:
                                print(Fore.YELLOW + "\nStarting up of rsyslog has succeeded!\n")
                            else:
                                print(Fore.RED + "\nFailed to start rsyslog...\n")
                        else:
                            print(Fore.RED + "\nFailed to enable rsyslog...\n")
                    else:
                        print(Fore.RED + "\nFailed to install Remote System Logging (rsyslog)...\nSkipping...\n")
                else:
                    print(Fore.WHITE + "\nNot installing Remote System Logging (rsyslog)...\nSkipping...\n")

                # Install Linux Containers
                lxc = input(Fore.WHITE + "[x] Do you wanna install Linux Containers (lxc/lxc)? [x] (y/N): ")
                if lxc.lower() == "y":
                    print(Fore.YELLOW + "#########################################")
                    print(Fore.YELLOW + "### Installing Linux Containers (LXC) ###")
                    print(Fore.YELLOW + "#########################################")
                    print(Style.RESET_ALL)
                    installLXC = f'echo {sudo_password} | sudo apt install lxc -y'
                    doInstallLXC = subprocess.Popen(installLXC, shell=True, text=True)
                    doInstallLXC.wait()

                    if doInstallLXC.returncode == 0:
                        print(Fore.YELLOW + "\nInstallation of LXC has succeeded!\nContinuing to install Bridge Utilities (brtctl)\n")
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
                        #os.system('sudo -u {} sudo apt install bridge-utils -y'.format(user))
                        installBrctl = f'echo {sudo_password} | sudo apt install bridge-utils -y'
                        doInstallBrctl = subprocess.Popen(installBrctl, shell=True, text=True)
                        doInstallBrctl.wait()

                        if doInstallBrctl.returncode == 0:
                            print(Fore.YELLOW + "\nInstallation of Bridge Utilities (brctl) has succeeded!\n")
                        else:
                            print(Fore.RED + "\nFailed to install Bridge Utilities (brctl)...\nSkipping...\n")
                        
                    else:
                        print(Fore.RED + "\nFailed to install LXC...\nSkipping...\n")

                    print(Fore.YELLOW + "#########################################")
                    print(Fore.YELLOW + "### Installing Linux Containers (LXD) ###")
                    print(Fore.YELLOW + "#########################################")
                    print(Style.RESET_ALL)
                    #os.system('sudo -u {} sudo /usr/bin/snap install lxd'.format(user))
                    #os.system('sudo -u {} sudo apt install lxc -y'.format(user))
                    installSNAP = f'echo {sudo_password} | sudo apt install snapd'
                    doInstallSNAP = subprocess.Popen(installSNAP, shell=True, text=True)
                    doInstallSNAP.wait()

                    if doInstallSNAP.returncode == 0:
                        print(Fore.YELLOW + "\nInstallation of SNAP has succeeded...\nEnabling SNAPD\n")
                        enableSNAP = f'echo {sudo_password} | sudo systemctl enable snapd'
                        doEnableSNAP = subprocess.Popen(enableSNAP, shell=True, text=True)
                        doEnableSNAP.wait()
                        if doEnableSNAP.returncode == 0:
                            print(Fore.YELLOW + "\nEnabling SNAPD has succeeded!\nStarting up SNAPD!\n")
                            startSNAP = f'echo {sudo_password} | sudo systemctl start snapd'
                            doStartSNAP = subprocess.Popen(startSNAP, shell=True, text=True)
                            doStartSNAP.wait()
                            if doStartSNAP.returncode == 0:
                                print(Fore.YELLOW + "\nStarting up SNAPD has succeeded!\nInstalling LXD using SNAP!\n")
                                installLXD = f'echo {sudo_password} | sudo /usr/bin/snap install lxd'
                                doInstallLXD = subprocess.Popen(installLXD, shell=True, text=True)
                                doInstallLXD.wait()
                                if doInstallLXD.returncode == 0:
                                    print(Fore.YELLOW + "\nInstallation of LXD has succeeded!\n")
                                else:
                                    print(Fore.RED + "\nFailed to install LXD...\n")
                            else:
                                print(Fore.YELLOW + "\nFailed to start SNAPD...\nSkipping to install LXD...\n")
                        else:
                            print(Fore.RED + "\nFailed to Enable SNAPD...\nSkipping to install LXD...\n")
                    else:
                        print(Fore.RED + "\nFailed to install SNAP...\nSkipping to install LXD...\n")
                else:
                    print(Fore.WHITE + "\nNot installing Linux Containers...\nSkipping...\n")

                # Install Docker
                docker = input(Fore.WHITE + "[x] Do you wanna install Docker? [x] (y/N): ")
                if docker.lower() == "y":
                    print(Fore.YELLOW + "### Installing Docker ###")
                    print(Style.RESET_ALL)
                    #os.system('sudo -u {} sudo apt install docker\.io -y'.format(user))
                    installDocker = f'echo {sudo_password} | sudo apt install docker\.io -y'
                    doInstallDocker = subprocess.Popen(installDocker, shell=True, text=True)
                    doInstallDocker.wait()

                    if doInstallDocker.returncode == 0:
                        print(Fore.YELLOW + "\nInstallation of Docker has succeeded!\n")
                    else:
                        print(Fore.RED + "\nFailed to install Docker...\nSkipping...\n")
                else:
                    print(Fore.WHITE + "\nNot installing Docker...\nSkipping...\n")

                # Install BeefProject
                beefXSS = input(Fore.WHITE + "[x] Do you wanna install Beef-XSS? [x] (y/N): ")
                if beefXSS.lower() == "y":
                    print(Fore.YELLOW + "### Installing Beef-XSS ###")
                    print(Style.RESET_ALL)
                    #os.system('sudo -u {} sudo apt install beef-xss -y'.format(user))
                    installBeefXSS = f'echo {sudo_password} | sudo apt install beef-xss -y'
                    doInstallBeefXSS = subprocess.Popen(installBeefXSS, shell=True, text=True)
                    doInstallBeefXSS.wait()

                    if doInstallBeefXSS.returncode == 0:
                        print(Fore.YELLOW + "\nInstallation of Beef-XSS has succeeded!\n")
                        print(Fore.YELLOW + "\nEnabling Beef-XSS...\n")
                        enableBeefXSS = f'echo {sudo_password} | sudo systemctl enable beef-xss'
                        doEnableBeefXSS = subprocess.Popen(enableBeefXSS, shell=True, text=True)
                        doEnableBeefXSS.wait()
                        if doEnableBeefXSS.returncode == 0:
                            print(Fore.YELLOW + "\nEnabling Beef-XSS has succeeded!\nStarting up Beef-XSS!\n")
                            startBeefXSS = f'echo {sudo_password} | sudo systemctl start beef-xss'
                            doStartBeefXSS = subprocess.Popen(startBeefXSS, shell=True, text=True)
                            doStartBeefXSS.wait()
                            if doStartBeefXSS.returncode == 0:
                                print(Fore.YELLOW + "\nStarting up Beef-XSS has succeeded!\nProceeding to configure Beef-XSS!\n")
                                # Locate Beef-XSS config file
                                # Save it to var $beefDir
                                
                                print(Fore.YELLOW + "\nChanging Beef-XSS login credentials...\n")
                                beefUser = input(Fore.YELLOW + "Enter new username for Beef-XSS UI login: ")
                                beefPasswd = getpass.getpass('Enter new Beef-XSS password: ')
                                editLoginCommand = f'echo {sudo_password} | sudo sed -i \'s/user\: beef/user\: {beefUser}/g\' /etc/beef-xss/config.yaml; echo {sudo_password} | sudo sed -i \'s/passwd\: beef/passwd\: {beefPasswd}/g\' /etc/beef-xss/config.yaml'
                                doEditLogin=subprocess.Popen(editLoginCommand, text=True, shell=True)
                                doEditLogin.wait()
                                if doEditLogin.returncode == 0:
                                    print(Fore.YELLOW + "\nChanging Beef-XSS Login credentials has succeeded!\n")
                                    ### Creating a directory to store current Beef-XSS Login credentials
                                    print(Fore.YELLOW + "\nCreating a directory:\n/home/user/Desktop/tools/beef-xss/\nTo store current Beef-XSS Login credentials\n")
                                    createLoginCommand = f'echo {sudo_password} | sudo mkdir /home/{user}/Desktop/tools/beef-xss'
                                    doCreateLogin=subprocess.Popen(createLoginCommand, text=True, shell=True)
                                    doCreateLogin.wait()
                                    if doCreateLogin.returncode == 0:
                                        print(Fore.YELLOW + "\nCreating a directory for Beef-XSS Login credentials file has succeeded!\n")
                                        print(Fore.YELLOW + "\nPurging existing login.txt at /home/user/Desktop/tools/beef-xss/login.txt\n")
                                        purgeLoginTxt = f'echo {sudo_password} | sudo rm -rf /home/{user}/Desktop/tools/beef-xss/login.txt;'
                                        doPurgeLoginTxt=subprocess.Popen(purgeLoginTxt, text=True, shell=True)
                                        doPurgeLoginTxt.wait()
                                        if doPurgeLoginTxt.returncode == 0:
                                            print(Fore.YELLOW + "\nPurging existing Login credentials file has succeeded!\n")
                                        else:
                                            print(Fore.RED + "\nFailed to purge existing Login credentials...\nSkipping...\n")
                                        ###
                                        print(Fore.YELLOW + "\nCreating login.txt at /home/user/Desktop/tools/beef-xss/login.txt\n")
                                        createLoginTxt = f'echo {sudo_password} | sudo touch /home/{user}/Desktop/tools/beef-xss/login.txt; echo {sudo_password} | sudo chmod 777 /home/{user}/Desktop/tools/beef-xss/login.txt'
                                        doCreateLoginTxt = subprocess.Popen(createLoginTxt, text=True, shell=True)
                                        doCreateLoginTxt.wait()
                                        if doCreateLoginTxt.returncode == 0:
                                            print(Fore.YELLOW + "\nCreating Login credentials file succeeded!\n")
                                            ###
                                            # Verifying Beef-XSS login credentials changes
                                            print(Fore.YELLOW + "\nSaving the current Beef-XSS login credentials...\n")
                                            saveLogin = f'user=$(echo {sudo_password} | sudo egrep "\s+user\:\s+(.*)" /etc/beef-xss/config.yaml); passwd=$(echo {sudo_password} | sudo egrep "\s+passwd\:\s+(.*)" /etc/beef-xss/config.yaml); echo {sudo_password} | sudo echo $user > /home/{user}/Desktop/tools/beef-xss/login.txt; echo {sudo_password} | sudo echo $passwd >> /home/{user}/Desktop/tools/beef-xss/login.txt; '
                                            doSaveLogin = subprocess.Popen(saveLogin, text=True, shell=True)
                                            doSaveLogin.wait()
                                            if doSaveLogin.returncode == 0:
                                                print(Fore.YELLOW + "\nSaving current Beef-XSS Login credentials has succeeded!\n")
                                                print(Fore.YELLOW + "Your current Beef-XSS login credentials are: ")
                                                readLogin = f'echo {sudo_password} | sudo cat /home/{user}/Desktop/tools/beef-xss/login.txt'
                                                doReadLogin = subprocess.Popen(readLogin, shell=True, text=True)
                                                doReadLogin.wait()
                                                #readLogin=os.system('sudo cat /home/phoenix/Desktop/tools/beef-xss/login.txt')
                                                if doReadLogin.returncode == 0:
                                                    print(Fore.YELLOW + "\nReading current Beef-XSS Login credentials has succeeded!\nYour current Beef-XSS Login is: ")
                                                    print(doReadLogin) 
                                                    ###
                                                    # Restart Beef-XSS
                                                    print(Fore.YELLOW + "\nRestarting Beef-XSS...\n")
                                                    restartBeefXSS = f'echo {sudo_password} | sudo systemctl restart beef-xss'
                                                    doRestartBeefXSS = subprocess.Popen(restartBeefXSS, shell=True, text=True)
                                                    doRestartBeefXSS.wait()
                                                    if doRestartBeefXSS.returncode == 0:
                                                        print(Fore.YELLOW + "\nRestarting Beef-XSS has succeeded!\n")
                                                        #os.system('sudo systemctl restart beef-xss')
                                                        print(Fore.YELLOW + "\n\nBeef-XSS is now accessible at http://127.0.0.1:3000/ui/authentication\n")
                                                    else:
                                                        print(Fore.RED + "\nFailed to restart Beef-XSS...\nSkipping...\n")
                                                    ###
                                                    ###
                                                else:
                                                    print(Fore.RED + "\nFailed to read current Beef-XSS Login credentials...\nSkipping...\n")
                                            else:
                                                print(Fore.RED + "\nFailed to save current Beef-XSS Login credentials...\nSkipping...\n")
                                        else:
                                            print(Fore.RED + "\nFailed to create Login credentials file...\n")
                                        ###
                                    else:
                                        print(Fore.RED + "\nFailed to create a directory for Beef-XSS Login credentials file...\n")
                                else:
                                    print(Fore.RED + "\nFailed to change Beef-XSS Login credentials...\nSkipping...\n")
                            else: 
                                print(Fore.RED + "\nStarting up Beef-XSS has failed...\nSkipping...\n")
                        else:
                            print(Fore.RED + "\nEnabling Beef-XSS has failed...\nSkipping...\n")
                    else:
                        print(Fore.RED + "\nFailed to install Beef-XSS...\nSkipping...\n")
                else:
                    print(Fore.WHITE + "\nNot installing Beef-XSS...\nSkipping...\n")
                  
                # Install OpenVAS
                openVAS = input(Fore.WHITE + "***OpenVAS can take up to 2 hours to install\n[x] Do you wanna install OpenVAS? [x] (y/N): ")
                if openVAS.lower() == "y":
                    print(Fore.YELLOW + "### Installing OpenVAS ###")
                    print(Style.RESET_ALL)
                    #os.system('sudo apt install openvas -y')
                    installOpenVAS = f'echo {sudo_password} | apt install openvas -y'
                    doInstallOpenVAS = subprocess.Popen(installOpenVAS, shell=True, text=True)
                    doInstallOpenVAS.wait()

                    if doInstallOpenVAS.returncode == 0:
                        print(Fore.YELLOW + "\nInstallation of OpenVAS has succeeded!\nContinuing to gvm-setup...\n")
                        gvmSetup = f'echo {sudo_password} | sudo gvm-setup'
                        doGvmSetup = subprocess.Popen(gvmSetup, shell=True, text=True)
                        doGvmSetup.wait()
                        if doGvmSetup.returncode == 0:
                            print(Fore.YELLOW + "\ngvm-setup has succeeded!\n")
                        else:
                            print(Fore.RED + "\ngvm-setup has failed...:(\n")
                    else:
                        print(Fore.RED + "\nFailed to install OpenVAS...\nCheck whether you've run PostgreSQL 15 && 14 PORTs update...\n")
                else:
                    print(Fore.WHITE + "\nNot installing OpenVAS...\nSkipping...\n")
        
        else:
            print(Fore.RED + "Failed to create tools directory... :(\nSkipping...\n")
    