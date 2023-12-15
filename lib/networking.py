# --------------
# Imports modules
# --------------
from . import user, sudo_password, distroName, initializeModules, Fore, sys, os, Back, Style, getpass, subprocess, re, time
from . import confirmNetworking

# Configure Linux networking at ease :)
def networkConfig():

    if confirmNetworking.lower() == "y" and user.lower() == 'root':
        
        # Configuring a network interface
        nic = input(Fore.YELLOW + f'Enter a network interface iface name [e.g. eth0]: ')
        regex = '^((\w+)|(\d+))$'
        validate = bool(re.match(regex, nic))
        #print(Fore.WHITE + f'validate.match: {validate.match}')
        #print(Fore.YELLOW + f'validate boolean: {validate}')
        
        # Store current time at the time of this module running
        thisTime = time.localtime(time.time())
        #print(Fore.WHITE + f'Time: {thisTime}')

        if validate == True:
            print(Fore.YELLOW + f'Succeeding in passing NIC name check, reasonable ? {validate} :)\nProceeding to configure NIC: {nic}\n')
            nicIp = input(f'Please enter {nic} IP [e.g. 192.168.0.1]: \n')
            ipRegex = '((10|1[0-9])|(17[1-9])|(19[1-9]))\.(([01]?[0-9][0-9]?|2[0-4][0-9]|25[0-5]))\.(([01]?[0-9][0-9]?|2[0-4][0-9]|25[0-5]))\.(([01]?[0-9][0-9]?|2[0-4][0-9]|25[0-4]))$'
            validateIp = re.match(ipRegex, nicIp)

            if validateIp:
                print(Fore.YELLOW + f'validateIp: {validateIp}\n')
                print(Fore.YELLOW + f'NIC IP: {nicIp} seems reasonable :)\nProceeding to configure {nic} Netmask...\n')
                nicNetmask = input(f'Please enter {nic} Netmask: [e.g. 255.255.255.0] \n')
                netmaskRegex = '^(0|128|192|224|240|248|252|254|255)\.(0|128|192|224|240|248|252|254|255)\.(0|128|192|224|240|248|252|254|255)\.(0|128|192|224|240|248|252|254|255)$'
                validateNetmask = re.match(netmaskRegex, nicNetmask)

                if validateNetmask:
                    print(Fore.YELLOW + f'{nic} Netmask: {nicNetmask} seems reasonable :)\nProceeding to configure {nic} gateway...\n')
                    nicGateway = input(f'Please enter {nic} Default Gateway [e.g. 192.168.0.254] \n')
                    gatewayRegex = '((10|1[0-9])|(17[1-9])|(19[1-9]))\.(([01]?[0-9][0-9]?|2[0-4][0-9]|25[0-5]))\.(([01]?[0-9][0-9]?|2[0-4][0-9]|25[0-5]))\.(([01]?[0-9][0-9]?|2[0-4][0-9]|25[0-4]))$'
                    validateGateway = re.match(gatewayRegex, nicGateway)

                    if validateGateway:
                        print(Fore.YELLOW + f'{nic} gateway: {nicGateway} seems reasonable :)\nProceeding to create this NIC...')
                        # Adding this NIC configuration to /etc/network/interfaces
                        addInterface = f'echo {sudo_password} | sudo printf "\nauto {nic}\niface {nic} inet static\naddress {nicIp}\nnetmask {nicNetmask}\ngateway {nicGateway}" >> /etc/network/interfaces'
                        doAddInterface = subprocess.run(addInterface, shell=True, text=True, capture_output=True)

                        if doAddInterface.returncode == 0:
                            print(Fore.YELLOW + f'Succeeded in adding {nic} to /etc/network/interfaces :)\nProceeding to restart networking.service using systemctl!\n')
                            # Restarting networking.service => systemctl stop networking.service
                            stopNetwork = f'echo {sudo_password} | sudo systemctl stop networking.service'
                            doStopNetwork = subprocess.run(stopNetwork, shell=True, text=True, capture_output=True)

                            if doStopNetwork.returncode == 0:
                                print(Fore.YELLOW + f'Succeeded in stopping networking.service :)\nProceeding to start networking.service\n')
                                startNetwork = f'echo {sudo_password} | sudo systemctl start networking.service'
                                doStartNetwork = subprocess.run(startNetwork, shell=True, text=True, capture_output=True)
                                if doStartNetwork.returncode == 0:
                                    print(Fore.YELLOW + f'Succeeded in starting networking.service :)\nProceeding to sudo route add default gw {nicGateway} {nic}\n')
                                    routeAdd = f'echo {sudo_password} | sudo route add default gw {nicGateway} {nic}'
                                    doRouteAdd = subprocess.run(routeAdd, shell=True, text=True, capture_output=True)
                                    if doRouteAdd.returncode == 0:
                                        print(Fore.YELLOW + f'Succeeded in adding default gateway: {nicGateway} for {nic} :)\nTesting internet connection...\n')
                                        pingTest = f'ping -c 10 8.8.8.8'
                                        doPingTest = subprocess.run(pingTest, shell=True, text=True, capture_output=True)

                                        if doPingTest.returncode == 0:
                                            print(Fore.YELLOW + f'Suceeded in ping test 8.8.8.8\nInternet seems is up :)\nCompleting this process...\n')
                                        else:
                                            print(Fore.RED + f'Failed ping test:\nping -c 10 8.8.8.8\nYou may tcheck against your default gw {nicGateway} manually...\nExiting...\n')
                                            sys.exit()

                                    else:
                                        print(Fore.RED + f'Failed to route add default gw {nicGateway} {nic} :(\nYou may manually do so by:\nsudo route add default gw {nicGateway} {nic}\nExiting...\n')
                                        sys.exit()

                                else:
                                    print(Fore.RED + f'Failed to start networking.service :(\nPlease manually start networking.service by:\nsudo systemctl start networking.service\nExiting...\n')
                                    sys.exit()

                            # If networking.service could not be stopped => Exit
                            else:
                                print(Fore.RED + f'Failed to stop networking.service\nPlease restart networking.service manually by\nsudo systemctl stop networking.service\nsudo systemctl start networking.service\nExiting...\n')
                                sys.exit()

                        else:
                            print(Fore.RED + f'Failed to create {nic} in /etc/network/interfaces :(\nExiting...')
                            sys.exit()

                    # If NIC Gateway is NOT valid => Exit
                    else:
                        print(Fore.RED + f'{nic} Gateway: {nicGateway} is NOT valid :(\nExiting...')
                        sys.exit()

                # If NIC Netmask is NOT valid => Exit
                else:
                    print(Fore.RED + f'{nicNetmask} is NOT a valid netmask :(...Proceeding...\n')

            # If NIC IP is not reasonable => Exit this module
            else:
                print(Fore.RED + f'valideIp: {validateIp}')
                print(Fore.RED + f'This NIC IP: {nicIp} seems NOT reasonable...\nSkipping...\n')
                sys.exit()

        # If NIC name is not reasonable => Exit this module
        elif validate != True:
            print(Fore.RED + f'Failed to pass NIC name check :(\nPlease enter a NIC name with String & Number only :)\ne.g. eth0\ne.g. ens1\nExiting processes...\n')
            sys.exit()

        # if nic.lower() != '':      
        #     print(Fore.YELLOW + "### Configuring Linux system network settings")
        #     print(Style.RESET_ALL)

        #     print(Fore.YELLOW + "\nItem1: Configuring Linux eth0 network configuration...")
        #     #os.system('sudo printf "auto eth0\niface eth0 inet static\naddress 192.168.76.133\nnetmask 255.255.255.0\nbroadcast 192.168.76.255\ngateway 192.168.76.2\n\nauto eth1\niface eth1 inet dhcp\nnetmask 255.255.248.0\ngateway 172.18.159.254\n\nauto lxcbr0\niface lxcbr0 inet static\naddress 192.168.76.141\nnetmask 255.255.255.0\nbroadcast 192.168.76.255\ngateway 192.168.76.2\n\nauto docker0\niface docker0 inet static\naddress 192.168.76.151\nnetmask 255.255.255.0\nbroadcast 192.168.76.255\ngateway 192.168.76.2" >> /etc/network/interfaces')

        #     eth0_ip = input("\nenter your eth0 IP: \ne.g. 192.168.76.101\n\n")
        #     eth0_netmask = input("\nenter your eth0 Netmask: \ne.g. 255.255.255.0\n\n")
        #     eth0_broadcast = input("\nenter your eth0 Broadcast address: \ne.g. 192.168.76.255\n\n")
        #     eth0_gateway = input("\nenter your eth0 default gateway IP: \ne.g. 192.168.76.2\n\n")

        #     # Temporarily changing mod for /etc/network/interfaces && /etc/resolv.conf
        #     chmodNetwork = f'echo {sudo_password} | sudo chmod 777 /etc/network/interfaces; sudo chown {user} /etc/network/interfaces'
        #     doChmodNetwork = subprocess.Popen(chmodNetwork, shell=True)
        #     doChmodNetwork.wait()
        #     print(Fore.YELLOW + "Temporarily chmod && chown for /etc/network/interfaces")
        #     print(doChmodNetwork.stdout)

        #     # Linux eth0 network config
        #     eth0Config = f'echo {sudo_password} | printf "### eth0 network config added at {thisTime} ###\nauto eth0\niface eth0 inet static\naddress {eth0_ip}\nnetmask {eth0_netmask}\nbroadcast {eth0_broadcast}\ngateway {eth0_gateway}\n### End of eth0 config ###" >> /etc/network/interfaces'
        #     doEth0Config = subprocess.Popen(eth0Config, shell=True)
        #     doEth0Config.wait()

        #     if doEth0Config.returncode == 0:
        #         print(Fore.YELLOW + "\nItem1: Configuring Linux eth0 network configuration has succeeded!")
        #     else:
        #         print(Fore.RED + "\nItem1: Configuring Linux eth0 network configuration has failed...:(")
        #         print(doEth0Config.stderr)

        #     # Printing /etc/network/interfaces
        #     printNetworkConfig = f'echo {sudo_password} | sudo cat /etc/network/interfaces'
        #     doPrintNetworkConfig = subprocess.Popen(printNetworkConfig, shell=True, text=True)
        #     doPrintNetworkConfig.wait()

        #     # Changing back mod for /etc/network/interfaces && /etc/resolv.conf
        #     print(Fore.YELLOW + "Changing back: \nchmod 644 /etc/network/interfaces\n&&\nchown root /etc/network/interfaces")
        #     chmodNetwork2 = f'echo {sudo_password} | sudo chmod 644 /etc/network/interfaces; sudo chown root /etc/network/interfaces'
        #     doChmodNetwork2 = subprocess.Popen(chmodNetwork, shell=True)
        #     doChmodNetwork2.wait()
        #     print(doChmodNetwork2.stdout)
        
        # else:
        #     print(Fore.YELLOW + "Not going to add eth0 config...\nSkipping...\n")

        ### Linux containers network configurations
        # lxc = input(
        #     Fore.YELLOW + "[x] Do you wanna configure lxcbr0? [x] (y/N): "
        # )
        # print(Style.RESET_ALL)

        # if lxc.lower() == "y":

        #     # Temporarily changing mod for /etc/network/interfaces && /etc/resolv.conf
        #     chmodNetwork = f'echo {sudo_password} | sudo chmod 777 /etc/network/interfaces; sudo chown {user} /etc/network/interfaces'
        #     doChmodNetwork = subprocess.Popen(chmodNetwork, shell=True)
        #     doChmodNetwork.wait()
        #     print(Fore.YELLOW + "Temporarily chmod && chown for /etc/network/interfaces")
        #     print(doChmodNetwork.stdout)

        #     # Start configuring Linux containers networks
        #     print(Fore.YELLOW + "\nItem2: Configuring Linux containers networks...\nAs you will be installing Linux containers as well\nPlease prepare to enter following details:\nFor Linux containers...\ni. lxcbr0 address\nii. lxcbr0 netmask\niii. lxcbr0 broadcast IP\niv. lxcbr0 gateway")
        #     lxcbr0_ip = input("\nenter your bridge interface - lxcbr0 IP: \ne.g. 192.168.76.101\n\n")
        #     lxcbr0_netmask = input("\nenter your lxcbr0 Netmask: \ne.g. 255.255.255.0\n\n")
        #     lxcbr0_broadcast = input("\nenter your lxcbr0 Broadcast address: \ne.g. 192.168.76.255\n\n")
        #     lxcbr0_gateway = input("\nenter your lxcbr0 default gateway IP: \ne.g. 192.168.76.2\n\n")

        #     # Linux containers networking
        #     lxcbr0Config = f'echo {sudo_password} | printf "### Linux containers network config added at {thisTime} ###\nauto lxcbr0\niface lxcbr0 inet static\naddress {lxcbr0_ip}\nnetmask {lxcbr0_netmask}\nbroadcast {lxcbr0_broadcast}\ngateway {lxcbr0_gateway}\n### End of Linux containers network config ###" >> /etc/network/interfaces'
        #     doLxcbr0Config = subprocess.Popen(lxcbr0Config, shell=True)
        #     doLxcbr0Config.wait()

        #     # Check Exit Code
        #     if doLxcbr0Config.returncode == 0:
        #         print(Fore.YELLOW + "\nItem2: Linux containers network configuration has succeeded!\n")
        #         print(Fore.YELLOW + "\nThe current /etc/network/interfaces has: \n")
        #         print(doPrintNetworkConfig.stdout)

        #     else:
        #         print(Fore.RED + "\nItem2: Linux containers network configuration has failed...:(")
        #         print(doLxcbr0Config.stderr)

        #     # Printing /etc/network/interfaces
        #     printNetworkConfig = f'echo {sudo_password} | sudo cat /etc/network/interfaces'
        #     doPrintNetworkConfig = subprocess.Popen(printNetworkConfig, shell=True, text=True)
        #     doPrintNetworkConfig.wait()

        #     if doPrintNetworkConfig == 0:
        #         print(Fore.YELLOW + "Printing current network config: \n")
        #         print(doPrintNetworkConfig.stdout)

        #     else:
        #         print(Fore.RED + "Failed to retrieve Network config...\n")
        #         print(doPrintNetworkConfig.stderr)

        #     # Changing back mod for /etc/network/interfaces && /etc/resolv.conf
        #     print(Fore.YELLOW + "Changing back: \nchmod 644 /etc/network/interfaces\n&&\nchown root /etc/network/interfaces")
        #     chmodNetwork2 = f'echo {sudo_password} | sudo chmod 644 /etc/network/interfaces; sudo chown root /etc/network/interfaces'
        #     doChmodNetwork2 = subprocess.Popen(chmodNetwork, shell=True)
        #     doChmodNetwork2.wait()
        #     print(doChmodNetwork2.stdout)
        
        # else:
        #     print(Fore.YELLOW + "Not going to add lxcbr0 config...\nSkipping...\n")
        
        # ###

        # # DNS settings
        # dns = input(
        #     Fore.YELLOW + "[x] Do you wanna add a nameserver? [x] (y/N): "
        # )
        # print(Style.RESET_ALL)

        # if dns.lower() == "y":

        #     print(Fore.YELLOW + "\nItem3: Adding a new DNS server to /etc/resolv.conf")
        #     print(Style.RESET_ALL)
        #     # os.system('sudo printf "nameserver 8.8.8.8\nnameserver 210.0.128.250\nnameserver 203.184.245.251" > /etc/resolv.conf')

        #     # Temporarily chmod && chown for /etc/resolv.conf
        #     chmodDNS = f'echo {sudo_password} | sudo chmod 777 /etc/resolv.conf; sudo chown {user} /etc/resolv.conf'
        #     doChmodDNS = subprocess.Popen(chmodDNS, shell=True)
        #     doChmodDNS.wait()
        #     print(doChmodDNS.stdout)

        #     dnsServer = input("\nEnter your DNS servername: \ne.g. 1.1.1.1\n\n")
        #     dnsConfig = f'echo {sudo_password} | su root; sudo printf "### DNS Servers added at {thisTime} ###\nnameserver {dnsServer}" >> /etc/resolv.conf'
        #     setDns = subprocess.Popen(dnsConfig, shell=True)
        #     setDns.wait()

        #     # Printing new DNS config
        #     dnsNewConfig = f'echo {sudo_password} | sudo cat /etc/resolv.conf'
        #     ReadDnsNewConfig = subprocess.Popen(dnsNewConfig, shell=True, text=True)

        #     if setDns.returncode == 0:
        #         print(Fore.YELLOW + "\nItem3: Adding a new DNS server succeeded!")
        #         print(Fore.YELLOW + "\nYour current DNS settings are: \n\n")
        #         print(ReadDnsNewConfig.stdout)
        #     else:
        #         print(Fore.RED + "\nItem3: Adding a new DNS server failed :(")
        #         print(Fore.RED + "\nYour current DNS settings are: \n\n")
        #         print(ReadDnsNewConfig.stdout)
            
        #     # Changing back mod for /etc/network/interfaces && /etc/resolv.conf
        #     chmodDNS2 = f'echo {sudo_password} | sudo chmod 644 /etc/resolv.conf; sudo chown root /etc/resolv.conf'
        #     doChmodDNS2 = subprocess.Popen(chmodDNS, shell=True)
        #     doChmodDNS2.wait()
        #     print(doChmodDNS2.stdout)
        
        # else:
        #     print(Fore.YELLOW + "Not going to add a DNS server...\nSkipping...\n")

        # # Restart Networking

        # restart = input(
        #     Fore.YELLOW + "[x] Do you wanna restart network? [x] (y/N): "
        # )
        # print(Style.RESET_ALL)

        # if restart.lower() == "y":
        #     print(Fore.YELLOW + "\nItem5: Restarting network service...\nRestarting networking.service")
        #     #os.system('sudo systemctl restart networking')
        #     restartNetwork = f'echo {sudo_password} | sudo systemctl restart networking'
        #     doRestartNetwork = subprocess.Popen(restartNetwork, shell=True)
        #     doRestartNetwork.wait()

        #     if doRestartNetwork.returncode == 0:
        #         print(Fore.YELLOW + "\nNetworking has restarted successfully!")
        #         print(doRestartNetwork.stdout)
        #     else:
        #         print(Fore.RED + "\nNetworking has failed to restart :(")
        #         print(doRestartNetwork.stderr)

        #     # Restart Networking Service
        #     #os.system('sudo systemctl restart networking.service')
        #     print(Fore.YELLOW + "\nRestarting networking.service ...")
        #     restartNetworkService = f'echo {sudo_password} | sudo systemctl restart networking.service'
            
        #     doRestartNetworkService = subprocess.Popen(restartNetworkService, shell=True)
        #     doRestartNetworkService.wait()
            
        #     if doRestartNetworkService.returncode == 0:
        #         print(Fore.YELLOW + "\nNetworking.service has restarted successfully!")
        #         print(doRestartNetworkService.stdout)
        #     else:
        #         print(Fore.RED + "\nNetworking.service has failed to restart :(")
        #         print(doRestartNetworkService.stderr)

        # else:
        #     print(Fore.YELLOW + "Not going to restart network...\nSkipping...\n")
    else:
        print(Fore.WHITE + "\nNot gonna configure network settings...\nSkipping...\n")
