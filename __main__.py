# IMPORTS
import os
from sys import argv as args, stderr
import time

# CONSTANTS

D_REPEAT_TIME = 5.0
REPEAT_TIME = D_REPEAT_TIME

D_EXEC_TIME = float('inf')
EXEC_TIME = D_EXEC_TIME

__version__ = '1.1.0'
__reldate__ = '2 November 2021'

def err(explanation: str):
    print('error:', explanation, file=stderr)

def print_version():
    print(f"You are using autofetch version {__version__} released at {__reldate__}")
    exit(0)

def print_help(ec: int):
    print("autofetch: A simple script to autofetch in git")
    print("")
    print("usage:")
    print(f"    {args[0]} [options]")
    print("")
    print("options:")
    print(f"    -t --time <time>         change execution time (type: float, default: {EXEC_TIME} s)")
    print(f"    -r --repeat-time <time>  change repeat time (type: float, default: {REPEAT_TIME} s)")
    print("    -h --help                show this help message and exit")
    print("    -V --version             show version info and exit")
    exit(ec)

curarg = 1
while len(args) > curarg:
    arg = args[curarg]
    if arg in ('-h', '--help'): print_help(0)
    elif arg in ('-V', '--version'): print_version()
    elif arg in ('-t', '--time'):
        if len(args) > curarg+1:
            EXEC_TIME = float(args[curarg+1])
            curarg += 1
        else:
            err(f"argument {arg} needs value <time>")
            print_help(1)
    elif arg in ('-r', '--repeat-time'):
        if len(args) > curarg+1:
            REPEAT_TIME = float(args[curarg+1])
            curarg += 1
        else:
            err(f"argument {arg} needs value <time>")
            print_help(1)
    else:
        err(f"unknown argument: {arg}")
        print_help(1)
    curarg += 1

t = time.time()

print('info: starting...')
try:
    while time.time()-t < EXEC_TIME:
        ec = os.system('git fetch')
        if ec != 0:
            err('git fetch encountered an error')
            exit(ec)
        time.sleep(REPEAT_TIME)
except KeyboardInterrupt: pass
print('info: closing...')
