for i in range(2,100):
    for j in range(2,i):
        if i % j == 0:
            break
    else:
        print(i,end='\t')

print("")

number = int(input())
current = 2
keys = set()
temp = {}

while True:
    if number == current:
        if current in keys:
            temp[current] += 1
        else:
            keys.add(current)
            temp[current] = 1
        break
    if number%current==0:
        number/=current
        if current in keys:
            temp[current] += 1
        else:
            keys.add(current)
            temp[current] = 1
    else:
        # if current == 2:
        #     current += 1
        # else:
        #     current += 2
        current = current+1 if current==2 else current+2

string = ""

for i in temp:
    string += f"{i}({temp[i]})*"
print(string[:-1])

def CtoF1(degreeC):
    print("攝氏",degreeC,"度可以轉換成華氏",degreeC*1.8+32,"度")

tC = eval(input("Enter degreeC:"))
CtoF1(tC)

def aver(*nums):
    return sum(nums)/len(nums)

def geo(*nums):
    ret = 1
    for i in nums:
        ret *= i
    return pow(ret,1/len(nums))

print(aver(1,4,5,6,7,3,8,4,9))
print(geo(1,4,5,6,7,3,8,4,9))