# --------------
# Imports modules
# --------------
from . import user, sudo_password, distroName, initializeModules, Fore, sys, os, Back, Style, getpass, subprocess, re, time
from . import confirmNetworking
from . import user, sudo_password
import ipcalc

# Configure Linux networking at ease :)
def networkConfig():

    if confirmNetworking.lower() == "y" and user.lower() == 'root':
        
        # Configuring a network interface
        nic = input(Fore.YELLOW + f'Enter a network interface iface name [e.g. eth0]: ')
        regex = '^((\w+)|(\d+))$'
        validate = re.match(regex, nic)
        #print(Fore.WHITE + f'validate.match: {validate.match}')
        #print(Fore.YELLOW + f'validate boolean: {validate}')
        
        # Store current time at the time of this module running
        thisTime = time.localtime(time.time())
        #print(Fore.WHITE + f'Time: {thisTime}')

        if validate:
            print(Fore.YELLOW + f'Succeeding in passing NIC name check, reasonable ? {validate} :)\nProceeding to configure NIC: {nic}\n')
            ip = input(f'Please enter {nic} IP [e.g. 192.168.0.1]: \n')
            ipRegex = '((10|1[0-9])|(17[1-9])|(19[1-9]))\.(([01]?[0-9][0-9]?|2[0-4][0-9]|25[0-5]))\.(([01]?[0-9][0-9]?|2[0-4][0-9]|25[0-5]))\.(([01]?[0-9][0-9]?|2[0-4][0-9]|25[0-4]))$'
            validateIp = re.match(ipRegex, ip)

            if validateIp:
                print(Fore.YELLOW + f'validateIp: {validateIp}\n')
                print(Fore.YELLOW + f'NIC IP: {ip} seems reasonable :)\nProceeding to configure {nic} Netmask...\n')
                netmask = input(f'Please enter {nic} Netmask: [e.g. 255.255.255.0] \n')
                netmaskRegex = '^(0|128|192|224|240|248|252|254|255)\.(0|128|192|224|240|248|252|254|255)\.(0|128|192|224|240|248|252|254|255)\.(0|128|192|224|240|248|252|254|255)$'
                print(Fore.YELLOW + f'\n\nCalculating Network Address IP...\n')
                # Calculate Network Address IP
                addr = ipcalc.IP(ip, mask=netmask)
                networkAddressIP = str(addr.guess_network())
                print(Fore.WHITE + f'\n\nCalculated Network Address IP: {networkAddressIP}\n')
                validateNetmask = re.match(netmaskRegex, netmask)

                if validateNetmask:
                    print(Fore.YELLOW + f'{nic} Netmask: {netmask} seems reasonable :)\n')
                    print(Fore.YELLOW + f'\n\nCalculating Network Address IP...\n')
                    # Converting Netmask to CIDR [e.g. /24]
                    cidr = sum(bin(int(x)).count('1') for x in netmask.split('.'))
                    print(Fore.YELLOW + f'\n\nCIDR: {cidr}\n') 
                    gateway = input(f'\n\nPlease enter {nic} Default Gateway [e.g. 192.168.0.254] \n')
                    gatewayRegex = '((10|1[0-9])|(17[1-9])|(19[1-9]))\.(([01]?[0-9][0-9]?|2[0-4][0-9]|25[0-5]))\.(([01]?[0-9][0-9]?|2[0-4][0-9]|25[0-5]))\.(([01]?[0-9][0-9]?|2[0-4][0-9]|25[0-4]))$'
                    validateGateway = re.match(gatewayRegex, gateway)

                    if validateGateway:
                        print(Fore.YELLOW + f'{nic} gateway: {gateway} seems reasonable :)\nProceeding to create this NIC...')
                        # Adding this NIC configuration to /etc/network/interfaces
                        addInterface = f'echo {sudo_password} | sudo printf "\nauto {nic}\niface {nic} inet static\naddress {ip}\nnetmask {netmask}\ngateway {gateway}" >> /etc/network/interfaces'
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
                                    print(Fore.YELLOW + f'Succeeded in starting networking.service :)\nProceeding to sudo ip route add {ip}/{cidr} via {gateway} dev {nic}\n')
                                    routeAdd = f'echo {sudo_password} | sudo ip route add {networkAddressIP}/{cidr} via {gateway} dev {nic}'
                                    doRouteAdd = subprocess.run(routeAdd, shell=True, text=True, capture_output=True)
                                    if doRouteAdd.returncode == 0:
                                        print(Fore.YELLOW + f'\n\nSucceeded in adding default gateway: {gateway} for {nic} :)\nTesting internet connection...\n')
            
                                    else:
                                        print(Fore.RED + f'\n\nFailed to ip route add {networkAddressIP}/{cidr} via {gateway} dev {nic} at:\n{thisTime} :(\n')
                                        print(Fore.RED + f'\n\nYou may manually add a route by:\nsudo ip route add {networkAddressIP}/{cidr} via {gateway} dev {nic}')
        
                                else:
                                    print(Fore.RED + f'\n\nFailed to start networking.service :(\nPlease manually start networking.service by:\nsudo systemctl start networking.service\nExiting...\n')
    
                            # If networking.service could not be stopped => Exit
                            else:
                                print(Fore.RED + f'\n\nFailed to stop networking.service\nPlease restart networking.service manually by\nsudo systemctl stop networking.service\nsudo systemctl start networking.service\nExiting...\n')

                        else:
                            print(Fore.RED + f'\n\nFailed to create {nic} in /etc/network/interfaces :(\nExiting...\n')

                    # If NIC Gateway is NOT valid => Exit
                    else:
                        print(Fore.RED + f'\n\n{nic} Gateway: {gateway} is NOT valid :(\nExiting...')

                # If NIC Netmask is NOT valid => Exit
                else:
                    print(Fore.RED + f'\n\n{netmask} is NOT a valid netmask :(...Proceeding...\n')

            # If NIC IP is not reasonable => Exit this module
            else:
                print(Fore.RED + f'\n\nvalideIp: {validateIp}')
                print(Fore.RED + f'\n\nThis NIC IP: {ip} seems NOT reasonable...\nSkipping...\n')

        # If NIC name is not reasonable => Exit this module
        elif not validate:
            print(Fore.RED + f'\n\nFailed to pass NIC name check :(\nPlease enter a NIC name with String & Number only :)\ne.g. eth0\ne.g. ens1\nExiting processes...\n')

    else:
        print(Fore.WHITE + f'\n\nNot gonna configure network settings...\nSkipping...\n')
