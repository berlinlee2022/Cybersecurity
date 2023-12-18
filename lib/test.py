import os
import colorama
from colorama import Fore, Back, Style
import subprocess
import getpass
import re
import sys
import time
import ipcalc, ipaddress

ip = input(Fore.WHITE + f'Enter a IP [e.g. 192.168.76.135]: ')
# Converting Netmask => CIDR
netmask = input(Fore.WHITE + f'Enter a netmask [e.g. 255.255.255.0]: ')
cidr = sum(bin(int(x)).count('1') for x in netmask.split('.'))
print(Fore.YELLOW + f'CIDR: {cidr}')

# Calculate Network Address IP
addr = ipcalc.IP(ip, mask=netmask)
networkAddressIP = str(addr.guess_network())
print(Fore.WHITE + f'Network Address IP: {networkAddressIP}')
