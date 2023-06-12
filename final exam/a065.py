# 提款卡
string = input()
cypher = ""

for i in range(len(string)-1):
    cypher += str(abs(ord(string[i])-ord(string[i+1])))



print(cypher)