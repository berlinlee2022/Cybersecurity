<h1>Usage</h1>
<br>
<h2>In order to communicate well when protecting our Full Stack applications</h2>
<h2>We need to know about what tools do 3rd party Penetration Testers use</h2>
<h2>2. Using Kali Linux as Docker Containers</h2>
<h2>docker build -t mykali -f ./Dockerfile .</h2>
<br>
<br>

## Running your mykali (docker image) with persistent volumes
## docker run -it --rm --name kali1 -v tools:/tools mykali
##
## Once you get into your litte kali1 container
## cd /tools 
## this is where you have your cybersecurity-kill-chains toolkit
## to bring havoc on the world :D
##
## To manage Docker persistent volume to be shared across kali containers 
## docker volume ls
## 
## You should see DRIVER local | VOLUME NAME tools
##
# 2. Using Kali as a Virtual Machine
## i. Upgrade Kali Repo
## bash upgrade.sh
##
## ii. Install Attack Tools
## bash install-tools.sh
##
## iii. Configure Tools
## bash configure.sh
##
## iv. Install Python3 dependencies
## bash install-pymodules.sh
##
## This repo helps you unleash Kali Linux & install tools much faster via Python automation, Bash, Docker :D
##
## cd ./Kali-Rebuild-Auto && sudo python3 ./main.py
## If your Kali Linux doesn't support this main.py, 
## Run the Shell Scripts instead
## bash./Kali-Rebuild-Auto/upgrade.sh;
## bash ./Kali-Rebuild-Auto/install-tools.sh;
# Kali Linux new build script
![Debian Linux](https://i.ytimg.com/vi/Y4umB6KqB4g/maxresdefault.jpg)
## Hi this script will do following tasks for you
##
## 1. Add a new priviledged user => Install open-source tools later on
## Enter new priviledged username 
## Confirm new priviledge user password
## Avoid using Kali root
## Add this priviledged user to /etc/sudoers
## Allow this priviledged user to run Bash
## new priviledged user=(ALL) ALL

## 2. Update PostgreSQL14, 15 Port values
### i. Changing port 5433 => 5432 for PostgreSQL15 to allow 'gvm-setup' during OpenVAS installation
### ii. Changing port 5432 => 5433 for PostgreSQL14 to allow 'gvm-setup' during OpenVAS installation

## 3. Update && Upgrade Kali's repository
## This is the most troublesome step when setting up a new Kali Linux...
### i. Add Kali archive keys
### ii. Update apt-key directory
### iii. Updating Kali's repo from HTTP to HTTPS to allow smooth apt update && apt upgrade -yuf; lateron
### deb https://http.kali.org/kali kali-rolling main non-free contrib" > /etc/apt/sources.list
### deb-src https://http.kali.org/kali kali-rolling main non-free contrib" >> /etc/apt/sources.list

## 4. Install a ton of open-source tools
## Create a tool directory for new priviledged user
## [Will not install these tools if choose not to create a new priviledged user]
## Install popular package managers (RPM, SNAP, NixNote2, Nautilus-dropbox, Keepassxc, Python3 PIP, DNF, GEM)
## 1N3/Sn1per
## PyAutoGUI
## Sherlock
## RedHawk
## Hping3
## Apache2
## SecList from https://github.com/danielmiessler/SecLists.git
## Visual Studio Code
## Guake - Drop Down Terminal (F12)
## Terminal Multiplexer - TMUX 
## NFS (Net File Share)
## XSSER
## EyeWitness
## Evil Win-RM
## PowerLine
## Remote System Logging (rsyslog)
## Linux Containers - lxc & lxd
## Docker
## BeefProject (via Apt) 
