# --------------
# Imports modules
# --------------
from . import user, sudo_password, distroName, initializeModules, Fore, sys, os, Back, Style, getpass, subprocess, re, time
from . import confirmNetworking
from . import user, sudo_password

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
            
                                    else:
                                        print(Fore.RED + f'Failed to route add default gw {nicGateway} {nic} :(\nYou may manually do so by:\nsudo route add default gw {nicGateway} {nic}\nExiting...\n')
        
                                else:
                                    print(Fore.RED + f'Failed to start networking.service :(\nPlease manually start networking.service by:\nsudo systemctl start networking.service\nExiting...\n')
    
                            # If networking.service could not be stopped => Exit
                            else:
                                print(Fore.RED + f'Failed to stop networking.service\nPlease restart networking.service manually by\nsudo systemctl stop networking.service\nsudo systemctl start networking.service\nExiting...\n')

                        else:
                            print(Fore.RED + f'Failed to create {nic} in /etc/network/interfaces :(\nExiting...')

                    # If NIC Gateway is NOT valid => Exit
                    else:
                        print(Fore.RED + f'{nic} Gateway: {nicGateway} is NOT valid :(\nExiting...')

                # If NIC Netmask is NOT valid => Exit
                else:
                    print(Fore.RED + f'{nicNetmask} is NOT a valid netmask :(...Proceeding...\n')

            # If NIC IP is not reasonable => Exit this module
            else:
                print(Fore.RED + f'valideIp: {validateIp}')
                print(Fore.RED + f'This NIC IP: {nicIp} seems NOT reasonable...\nSkipping...\n')

        # If NIC name is not reasonable => Exit this module
        elif validate != True:
            print(Fore.RED + f'Failed to pass NIC name check :(\nPlease enter a NIC name with String & Number only :)\ne.g. eth0\ne.g. ens1\nExiting processes...\n')

    else:
        print(Fore.WHITE + "\nNot gonna configure network settings...\nSkipping...\n")
