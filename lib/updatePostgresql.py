# Imports modules
# --------------
from . import user, sudo_password, distroName, initializeModules, Fore, sys, os, Back, Style, getpass, subprocess, re
# Import module specific variables
from . import thisTime
from . import confirmUpdatePostgres
from . import user, sudo_password

def updatePostgres():

    if confirmUpdatePostgres is not None and confirmUpdatePostgres.lower() == 'y':

        print(Fore.YELLOW + "\nUpdating PosgreSQL 15 port from port 5433 to port 5432...\n")
        
        updatePostgres15 = f'echo {sudo_password} | sudo sed -i \'s/port \= 5433/port \= 5432/g\' /etc/postgresql/15/main/postgresql.conf'
        doUpdatePostgres15 = subprocess.Popen(updatePostgres15, shell=True)
        doUpdatePostgres15.wait()

        if doUpdatePostgres15.returncode == 0:
            print(Fore.YELLOW + "Updating PosgreSQL 15 port from port 5433 to port 5432\nhas succeeded!\n")
            print(doUpdatePostgres15.stdout)
        else:
            print(Fore.RED + "Updating PosgreSQL 15 port from port 5433 to port 5432\nhas failed... :(")
            print(doUpdatePostgres15.stderr)

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
        print(Fore.RED + f'Could NOT confirm {confirmUpdatePostgres} is Y\nSkipping...\n')
    
