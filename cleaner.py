import os
import subprocess

# Cleaning screen function

def clean():
    if os.name == ('ce', 'nt', 'dos'):
        os.system('cls')
    elif os.name == 'posix':
        os.system('clear')
    else:
        print('\n' * 120)
