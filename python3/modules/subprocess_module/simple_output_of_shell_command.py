#!/usr/bin/python3



import subprocess



output = subprocess.run('ls -a', shell=True)


print(output)



