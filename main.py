# ==============
# Import Colorama
from colorama import Fore, Back, Style
# Importing modules from ./lib
from lib import addUser, changeKeyboardLayout, networking, updatePostgresql, changeRootPasswd, upgrade, installTools, cleanup
# --------------
# Imports module 'webdriver' from 'selenium'
# Trying to automate some key send actions in Firefox
# --------------
#from selenium import webdriver
#from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.common.action_chains import action_chains
#from selenium.webdriver.firefox.firefox_binary import firefox_binary
#binary = firefox_binary('/usr/bin/firefox')
#browser = webdriver.firefox(firefox_binary=binary)
# ===============

# Add new Low Privilege User Account
#print(Fore.WHITE + "### Creating a Low Priv User ###")
#print(Style.RESET_ALL)
addUser.addUser()

# Changing Keyboard Layout
# print(Fore.WHITE + "Changing Keyboard Layout :)")
# import changeKeyboardLayout
changeKeyboardLayout.changeKeyboardLayout()

# Network configuration
#print(Fore.WHITE + "Configuring local Network settings")
networking.networkConfig()

# Update PostgreSQL config :)
#print(Fore.WHITE + "Updating PostgreSQL ports :)")
#updatePostgresql.updatePostgres()
    
# Change Root Pwd
#print(Fore.WHITE + "Changing ROOT password :)")
#changeRootPasswd.changeRootPasswd()

# Update & Upgrade
#print(Fore.WHITE + "Doing apt update && apt upgrade :)")
#upgrade.upgrade()

# Installing Tools
#print(Fore.WHITE + "Installing PenTest tools :)")
#installTools.installTools()

# Install Optional Tools
#import optional-tools
#optional-tools.installOptTools()

# Cleaning Up
#cleanup.cleanup()

# --------------
# Function Calls
# --------------

# networking()
# addUser()
# changeRootPwd()
# changeKeyboardLayout()
# upgrade()
# installTools()
# installOptTools()
# cleanup()
# -
