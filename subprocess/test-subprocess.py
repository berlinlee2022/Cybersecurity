import subprocess

command1 = f'ls -la'
p1 = subprocess.run(
    command1, 
    shell=True, 
    stdout=subprocess.PIPE, 
    stderr=subprocess.PIPE,
    text=True)

if p1.returncode == 0:
    print(f'\n')
    print(f'{p1.stdout}')
else:
    print(f'\n')
    print(f'{p1.stderr}')
    
