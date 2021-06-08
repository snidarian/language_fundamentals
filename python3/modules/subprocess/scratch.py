#!/usr/bin/python3



import subprocess



output = subprocess.run('ls -a', shell=True, cwd='/home/')





print(output.args)



