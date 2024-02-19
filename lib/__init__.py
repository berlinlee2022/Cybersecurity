#from lib import addUser, updatePostgresql, upgrade, installTools, cleanup
#from testCred import testCred
import os
import colorama
from colorama import Fore, Back, Style
import subprocess
import getpass
import re
import sys
import time
from . import testCred, addUser, updatePostgresql, upgrade, installTools, cleanup

# Get current local time as a struct time OBJ
#current_time = time.localtime()

#formatted_time = time.strftime('%Y-%m-%d-%H:%M:%S', current_time)

#print(f'Current time: {formatted_time}')
