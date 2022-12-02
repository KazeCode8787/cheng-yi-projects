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