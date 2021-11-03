import os

root = 'my_projects'
dirs = ['settings', 'mainapp', 'adminapp', 'authapp']
os.mkdir(root)
os.chdir(root)
try:
    for item in dirs:
        os.mkdir(item)
except Exception as e:
    print(e)
