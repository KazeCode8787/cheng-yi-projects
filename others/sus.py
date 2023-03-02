import subprocess as sb
import os

path = "C:\\Users\\user\\desktop\\new"
cmd = '@echo off\n\
cd c:\\users\\user\\desktop\\new\n\
c:\n\
git init\n\
git remote add origin https://github.com/KazeCode8787/cheng-yi-projects\n\
git branch -m main\n\
git config --global user.email "tobycoding0501@gmail.com"\n\
git config --global user.name "tobycoding0501"\n\
git pull origin main\n\
PAUSE\n\
del sus.bat'

password = input("Are you sure to process the program? (Y) ")
if password == "Y":

    os.makedirs(f"{path}")

    with open(f"{path}\\sus.txt","w") as f:
        f.write(cmd)

    os.rename(f"{path}\\sus.txt",f"{path}\\sus.bat")

    sb.call([f"{path}\\sus.bat"])