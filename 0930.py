import math
import random as r
m = math

print(math.radians(90))
print(max(10,8,-9,-100,77,50,28))
print(min(10,8,-9,-100,77,50,28))
print(10*10*math.pi)
print(math.cos(math.radians(60)))
print(math.sqrt(7))
print(math.gcd(616,1331))

x = math.log(2,10)
y = math.log(3,10)

result = pow(10,2*x+3*y+1)
print("結果為：",result)

print(r.randint(1,10))
print(r.randint(1,10))

print(r.random())
print(r.random())

L = [1,2,3,4,5]
r.shuffle(L)
print(L)
print(r.choice(L))

num = r.randint(1,3)
answer = eval(input("猜數字(1~3)："))
print(num,"==",answer,"is",num==answer)

s =eval(input("請輸入正六邊形的邊長："))
area = 6*s*s/(4*m.tan(m.pi/6))
print("邊長",s,"的正六邊形面積：",area)