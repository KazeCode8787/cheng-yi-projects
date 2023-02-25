import calendar as c,time as t

print(c.calendar(2022))
print(c.calendar(2023))
print(c.month(2022,1))

# def isLeapYear(year):
#     if (year%4==0 and year%100!=0) or year%400==0:
#         return True
#     else:
#         return False

isLeapYear = lambda year: True if (year%4==0 and year%100!=0) or year%400==0 else False

for i in range(2000,2051):
    if isLeapYear(i):
        print(i)

secs = eval(input("請輸入要倒數的秒數"))

for i in range(secs,0,-1):
    print(f"倒數 {i} 秒...")
    t.sleep(1)

print("時間到！")

def isPrime(num):
    for i in range(2,num):
        if num%i==0:
            return False
    else:
        return True

for i in range(2,101):
    if isPrime(i):
        print(i)

# def Sum(P,r,t):
#     return P*(1+r*t)

Sum = lambda P,r,t:P*(1+r*t)
a = int(input("本金"))
b = float(input("年利率"))
C = int(input("年數"))


print(Sum(a,b,C))

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