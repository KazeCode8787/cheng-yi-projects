# 金字塔
a = int(input())
for i in range(1,a+1):
    print(f"{' '*(a-i)}{'*'*(2*i-1)}")

    
# 九九乘法
for i in range(1,10):
    for j in range(1,10):
        print(f"{i}*{j}={i*j}",end="\t")
    print()

# (1/2)^1+(1/2)^2....
ans = 0
for i in range(1,9):
    ans += (1/2)**i

print(ans)

# 1+1/2+1/3+...
ans = 0
for i in range(1,11):
    ans += 1/i

print(ans)

# 阿姆斯壯數
ra1, ra2 = map(int,input().split())
check = False
for i in range(ra1,ra2):
    j = str(i)
    length = len(j)
    ctn = 0
    for k in j:
        ctn += int(k)**length
    if ctn == i:
        print(i,end=" ")
        check = True
if not check:
    print('none')

# 質因數分解
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
        current = current+1 if current==2 else current+2
string = ""
for i in temp:
    string += f"{i}({temp[i]})*"
print(string[:-1])


# 最大公因數
def GCD(n,m):
    assert m>n
    if m%n==0:
        return n
    else:
        return GCD(n,m%n)

print(GCD(5,100))


# 費氏數列
def fibo(n):
    if n==1 or n==2:
        return 1
    else:
        return fibo(n-1)+fibo(n-2)

n = 16# 印出前16-1項
for i in range(1,n):
    print(fibo(i),end="\t")


#質因數判斷
def isPrime(num):
    for i in range(2,num):
        if num%i==0:
            return False
    else:
        return True

for i in range(2,101):
    if isPrime(i):
        print(i)

# 2~99的質數
for i in range(2,100):
    for j in range(2,i):
        if i % j == 0:
            break
    else:
        print(i,end='\t')

print()