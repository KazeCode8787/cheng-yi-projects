# 質因數之和
try:
    while True:
        num = int(input())
        ans = 0
        i = 2
        while i <= num:
            while num % i==0:
                num /= i
                ans += i

            if i == 2:
                i+=1
            else:
                i+=2

        print(ans)

except:
    pass