# Q1
for i in range(1,10):
    for j in range(1,10):
        print(f"{i}*{j}={i*j}",end="\t")

    print()

# Q2
ctn = 0
for i in range(1,9):
    ctn += (1/2)**i

print(ctn)

# Q3
num = input()
ans = 1
for i in num:
    ans *= int(i)

print(ans)

# Q4
def fibo(num):
    if num==1 or num==2:
        return 1
    else:
        return fibo(num-1) + fibo(num-2)

for i in range(1,16):
    print(fibo(i),end=" ")