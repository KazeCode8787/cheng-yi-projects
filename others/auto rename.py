import os
import datetime
path = "./"

print("用\"%d\"來當作流水編號\n\
用\"%N\"來輸入姓名\n\
用\"%n\"來輸入座號\n\
用\"%t\"來輸入日期")
inpt = input()
date = datetime.datetime.now()
i = 0
name = "Your name here" #在雙括號內輸入姓名
number = "Your seat number here"    #在雙括號內輸入座號

for file in os.listdir(path):
    startName, endName = file.split('.')
    if endName == "py":
        continue
    i += 1
    inp = inpt.replace("%d",str(i)).replace("%n",number).replace("%N",name).replace("%t",str(date.strftime("%m-%d")))
    os.rename(f"{path}{startName}.{endName}",f"{path}{inp}.{endName}")

