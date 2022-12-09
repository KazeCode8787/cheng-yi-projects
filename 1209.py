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