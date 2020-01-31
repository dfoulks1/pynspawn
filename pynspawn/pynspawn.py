#!/usr/bin/python3 -B

import subprocess

def order(machineID, cmd):
    try:
        command = ['systemd-nspawn', '--timezone', 'off', '-M', machineID]
        command.extend(cmd.split(' '))
        subprocess.check_call(command)
    except subprocess.CalledProcessError as e:
        print(e)
        
def daemonize(name):
    try: 
        subprocess.check_call(['systemctl', 'enable', 'systemd-nspawn@' + name + '.service'])
        subprocess.check_call(['systemctl', 'start', 'systemd-nspawn@' + name + '.service'])
    except subprocess.CalledProcessError as e:
        print(e)
