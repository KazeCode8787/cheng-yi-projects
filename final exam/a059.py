# 完全平方數
T = int(input())

for _ in range(T):
    a = int(input())
    b = int(input())
    sum_ = 0
    for n in range(a,b+1):
        if pow(n,0.5) == int(pow(n,0.5)):
            sum_ += n
    print(f"Case {_+1}: {sum_}")