import subprocess
import time
import os

'''
p=subprocess.run(["pwd"])
w = subprocess.run('cd ..', shell=True)
print (w.returncode)
p=subprocess.run(["pwd"])
'''

wd = os.getcwd()
subprocess.run("pwd")
os.chdir(os.path.expanduser(".."))
subprocess.run("pwd")
os.chdir(wd)
