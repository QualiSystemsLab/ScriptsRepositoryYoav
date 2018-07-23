import os
import subprocess

base_folder = os.getcwd()
proc = subprocess.Popen('cmd.exe', stdin = subprocess.PIPE, stdout = subprocess.PIPE)
folders = [folder for folder in os.listdir(os.getcwd()) if not folder.__contains__('.')]
for folder in folders:
    os.chdir('{0}\{1}'.format(base_folder ,folder))
    print os.popen('shellfoundry install').read()
    print os.getcwd()
pass