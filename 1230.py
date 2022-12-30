a = int(input())

for i in range(1,a+1):
    print(f"{' '*(a-i)}{'*'*(2*i-1)}")

for i in range(1,10):
    for j in range(1,10):
        print(f"{i}*{j}={i*j}",end="\t")
    print()

ans = 0
for i in range(1,9):
    ans += (1/2)**i

print(ans)

ans = 0
for i in range(1,11):
    ans += 1/i

print(ans)

def GCD(n,m):
    assert m>n
    if m%n==0:
        return n
    else:
        return GCD(n,m%n)

print(GCD(5,100))

def fibo(n):
    if n==1 or n==2:
        return 1
    else:
        return fibo(n-1)+fibo(n-2)

for i in range(1,16):
    print(fibo(i),end="\t")