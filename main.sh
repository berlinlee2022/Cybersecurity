#!/bin/bash

if [[ ${UID} -ne 0 ]];
then
    echo "You aren't ROOT";
    echo "Exiting...";
    exit 1;
else
    echo "You are ROOT";
    echo "Proceeding...";
fi

echo "chmod 777 for ./upgrade.sh ./install-tools.sh ./install-pymodules.sh ./configure.sh";

sudo chmod777 ./upgrade.sh;
sudo chmod777 ./install-tools.sh;
sudo chmod 777 ./install-pymodules.sh;
sudo chmod 777 ./configure.sh;

upgrade=$(sudo bash ./upgrade.sh);
if [[ ${?} -eq 0 ]];
then
    echo "Succeeded in updating Kali Repository :D";
    echo "Proceeding to install Kali tools ;)";
    installTools=$(sudo bash ./install-tools.sh);
    if [[ ${?} -eq 0 ]];
    then
        echo "Succeeded in install Kali Tools :D";
        echo "Proceeding to install Python3 modules...";
        
    else
        echo "Failed to install Kali tools :(";
        echo "Exiting...";
        exit 1;
    fi
else
    echo "Failed to update Kali Repository :(";
    echo "Exiting with 1";
    exit 1;
fi

installModules=$(sudo bash ./install-pymodules.sh);
if [[ ${?} -eq 0 ]];
then
    echo "Succeeded in install Python3 modules :D";
    echo "Proceeding to configure installed Kali Tools :D";
else   
    echo "Failed to install Python3 modules :(";
    echo "Skipping...";
fi

configureTools=$(sudo bash ./configure.sh);
if [[ ${?} -eq 0 ]];
then
    echo "Succeeded in configuring Kali Tools :D";
    echo "Exiting...";
    exit 0;
else   
    echo "Failed to configure Kali Tools :(";
    echo "Exiting with 1";
    exit 1;
fi