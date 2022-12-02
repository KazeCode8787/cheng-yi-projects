import random as ra
result1, result2 = '',''

for i in range(1,10):
    result1 = ''
    for j in range(1,10):
        result1 += f"{i}*{j}={i*j}\t"

    result2 += result1+'\n'

print(result2)

SUM = 0
for i in range(2,101,2):
    SUM += i
print(SUM)

n = eval(input("請輸入金字塔的高度(1~30)："))

for i in range(1,n+1):
    print(f"{' '*(n-i)}","*"*(2*i-1))

ans = input("請輸入\"快樂\"的英文")

while ans.upper()!= "HAPPY":
    ans = input("答錯了")
else:
    print("答對了")

num = eval(input("請輸入1~10的正整數"))

result = 1
i = 1
while i <= num:
    result *= i
    i+=1
print(f"{num}乘階為{result}")


num = ra.randint(1,10)
ans = -1
while ans != num:
    ans = eval(input("請猜數字1~10"))
    if ans > num:
        print("Too big")
    elif ans<num:
        print("Too small")
    else:
        print("Correct")

money = float(25000.0)
years = 0
while money < 50000:
    money *= 1.03
    years += 1
print(years)