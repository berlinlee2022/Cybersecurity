import subprocess
from colorama import Fore

command1 = f'ls -la'
# p1 = subprocess.run(
#     command1, 
#     shell=True, 
#     stdout=subprocess.PIPE, 
#     stderr=subprocess.PIPE,
#     text=True)

p1 = subprocess.Popen(
    command1,
    shell=True,
    text=True,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE
)

p1_out, p1_err = p1.communicate()

if p1.returncode == 0:
    print(f'\n')
    print(Fore.WHITE + f'{p1_out}')
else:
    print(f'\n')
    print(Fore.RED + f'{p1_err}')
    
    
