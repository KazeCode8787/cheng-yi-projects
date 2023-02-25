def GCD(m,n):
    if m%n==0:
        return n
    else:
        return GCD(n,m%n)

print(f"87和1080的最大公因數為 {GCD(84,1080)}")

def fibo(n):
    assert n>0 and type(n)==int
    if n==1 or n==2:
        return 1
    else:
        return fibo(n-1)+fibo(n-2)

for i in range(1,16):
    print(fibo(i),end="\t")
