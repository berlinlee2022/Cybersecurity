# --------------
# Imports modules
# --------------
import os
from colorama import Fore, Back, Style
import subprocess
import getpass

def updatePostgres():

    update = input(Fore.WHITE + "[x] Do you wanna update any Postgres config? [x] (y/N): ")
    print(Style.RESET_ALL)

    if update.lower() == "y":

        postgres15 = input(
            Fore.WHITE + "[x] Do you wanna update PostgreSQL ports for Postgres15?[x] (y/N): "
        )
        print(Style.RESET_ALL)

        if postgres15.lower() == "y": 
            sudo_password = getpass.getpass(prompt='Please enter your sudo password: ')
        
            print(Fore.WHITE + "\nUpdating PostgreSQL 15 port no...\n")
            # Changing port 5433 => 5432 for PostgreSQL15 to allow update
            #os.system('sudo sed -i \'s/port \= 5433/port \= 5432/g\' /etc/postgresql/15/main/postgresql.conf')
            print(Fore.YELLOW + "\nUpdating PosgreSQL 15 port from port 5433 to port 5432...\n")
            print(Style.RESET_ALL)
            updatePostgres15 = f'echo {sudo_password} | sudo sed -i \'s/port \= 5433/port \= 5432/g\' /etc/postgresql/15/main/postgresql.conf'
            doUpdatePostgres15 = subprocess.Popen(updatePostgres15, shell=True)
            doUpdatePostgres15.wait()

            if doUpdatePostgres15.returncode == 0:
                print(Fore.YELLOW + "Updating PosgreSQL 15 port from port 5433 to port 5432\nhas succeeded!\n")
                print(doUpdatePostgres15.stdout)
            else:
                print(Fore.RED + "Updating PosgreSQL 15 port from port 5433 to port 5432\nhas failed... :(")
                print(doUpdatePostgres15.stderr)
        
        else:
            print(Fore.WHITE + "Not updating PostgreSQL15 port number...\nSkipping...\n")

        postgres14 = input(
            Fore.WHITE + "[x] Do you wanna update PostgreSQL ports for Postgres14? [x] (y/N): "
        )
        print(Style.RESET_ALL)

        if postgres14.lower() == "y": 

            print(Fore.WHITE+ "Updating PosgreSQL 14 port from port 5432 to port 5433")
            print(Style.RESET_ALL)

            # Changing port 5432 => 5433 for PostgreSQL14 to allow update
            #os.system('sudo sed -i \'s/port \= 5432/port \= 5433/g\' /etc/postgresql/15/main/postgresql.conf')
            updatePostgres14 = f'echo {sudo_password} | sudo sed -i \'s/port \= 5432/port \= 5433/g\' /etc/postgresql/15/main/postgresql.conf'

            doUpdatePostgres14 = subprocess.Popen(updatePostgres14, shell=True)
            doUpdatePostgres14.wait()

            if doUpdatePostgres14 == 0:
                print(Fore.YELLOW + "\nUpdating PosgreSQL 14 port from port 5432 to port 5433 has succeeded!\n")
                print(Style.RESET_ALL)
                print(doUpdatePostgres14.stdout)
                
            else:
                print(Fore.RED + "\nFailed to update PostgreSQL 14 port no. :(\n")
                print(doUpdatePostgres14.stderr)
                print(Style.RESET_ALL)
        
        else:
            print(Fore.WHITE + "Not updating PostgreSQL14 port no...\nSkipping...\n")

        restart = input(
            Fore.WHITE + "\n[x] Do you wanna restart PostgreSQL service? [x] (y/N): "
        )
        print(Style.RESET_ALL)

        if restart.lower() == "y": 
            # Restart PostgreSQL service
            print(Fore.YELLOW + "\nRestarting PostgreSQL service...\n")
            #os.system('sudo systemctl restart postgresql')
            restartPostgres = f'echo {sudo_password} | sudo systemctl restart postgresql'
            doRestartPostgres = subprocess.Popen(restartPostgres, shell=True)
            doRestartPostgres.wait()

            if doRestartPostgres.returncode == 0:
                print(Fore.YELLOW + "\nRestarting PostgreSQL service has succeeded!\n")
                print(doRestartPostgres.stdout)
            else:
                print(Fore.RED + "\nRestarting PostgreSQL service has failed...:(\n")
                print(doRestartPostgres.stderr)
                print(Style.RESET_ALL)
        else:
            print(Fore.WHITE + "\nNot gonna restart PostgreSQL service...\nSkipping...\n")
    
    else:
        print(Fore.WHITE + "\nNot gonna update Postgres config at all...\nSkipping...\n")
