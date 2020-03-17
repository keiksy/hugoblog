import os, sys

if os.getcwd() != '/Users/cai/Desktop/Blog/keiksyblog':
    sys.exit("Place this script to Hugo root folder!")

os.system('git add .')
os.system('git commit -m \'new post\'')
os.system('git push')
os.system('hugo -d ~/Blog/public')

os.chdir('../public')
os.system('git add .')
os.system('git commit -m \'new post\'')
os.system('git push')

