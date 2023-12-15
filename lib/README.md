# Usage
## git clone this repo
## cd ./kali-new-build
## python3 ./new-kali.py

## =========================================================================================================================
# Kali Linux new build script
## Hi this script will do following tasks for you

## 1. Configure local linux system network settings
### i. Set up eth0
### ii. DNS nameserver 8.8.8.8 nameserver 210.0.128.250 nameserver 203.184.245.251 >> /etc/resolv.conf
### iii. route add default gw

## 2. Update PostgreSQL14, 15 Port values
### i. Changing port 5433 => 5432 for PostgreSQL15 to allow 'gvm-setup' during OpenVAS installation
### ii. Changing port 5432 => 5433 for PostgreSQL14 to allow 'gvm-setup' during OpenVAS installation

## 3. Create a new privileged user
### i. sudo adduser <user>
### ii. Add this user to sudoers
### iii. Allow this user to run /bin/bash

## 4. Change Root password

## 5. Change Keyboard layout

## 6. Update && Upgrade Kali's repository
### i. Add Kali archive keys
### ii. Update apt-key directory
### iii. Updating Kali's repo from HTTP to HTTPS to allow smooth apt update && apt upgrade -yuf; lateron
### deb https://http.kali.org/kali kali-rolling main non-free contrib" > /etc/apt/sources.list
### deb-src https://http.kali.org/kali kali-rolling main non-free contrib" >> /etc/apt/sources.list

## 7. Install a ton of tools
## i. Create a tool directory
## ii. Install package managers (SNAP, NixNote2, Nautilus-dropbox, Keepassxc, Python3 PIP, DNF, GEM)

## Recon Tools
## iii. Sn1per
## iv. PyAutoGUI
## v. Sherlock
## vi. RedHawk
## vii. Hping3

## Optional Tools
## viii. Apache2
## ix. SecList from https://github.com/danielmiessler/SecLists.git
## x. Visual Studio Code
## xi. Guake - Drop Down Terminal (F12)
## xii. TMUX
## xiii. Terminal Multiplexer - TMUX 
## xiv. NFS (Net File Share)
## xv. XSSER
## xvi. EyeWitness
## xvii. Evil Win-RM
## xviii. PowerLine
## xix. Package Manager (RPM)
## xx. Remote System Logging (rsyslog)
## xxi. Linux Containers - lxc & lxd
## xxii. Docker
## xxiii. BeefProject (via Apt) 
