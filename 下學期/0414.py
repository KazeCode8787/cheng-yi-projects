import shutil as sh
import os

path = "C://sus1.txt"
path2 = "C://sus2.txt"

with open(path,'w') as f:
    f.write("ajskdlsajd\nksadksa;ldkasjd\njiowjdqojddsd\nkadjksjd\nsad")

sh.copy(path,path2)

print("sus1.txt已被複製到sus2.txt")

with open(path,'r') as f:
    data = f.read()
    size = len(data)


lines = data.count("\n")+1

print(f"sus1.txt檔案有{lines}行{size}字")
