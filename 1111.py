x=15
y=10
if x > y:
   z = x - y
   print("x比y大",z)
score = eval(input("請輸入數學分數(0 ~ 100)："))
if score >= 60:
             print ("及格！")
else:
             print ("不及格！")
score = eval(input("請輸入數學分數(0 ~ 100)："))
if score >= 90:
    print("優等")
elif score < 90 and score >= 80:
    print("甲等")
elif score < 80 and score >= 70:
    print("乙等")
elif score < 70 and score >= 80:
    print("丙等")
else :
    print ("不及格")
print(list(range(5)))
print(list(range(1,10,2)))
print(list(range(1,-10,-2)))
sum = 0
for i in range(1,7):
    sum = sum + i
else:
    print("總和等於",sum)
num=100
for i in range(num):
    if i>0:
        if i%13==0:
            print(i)
a=0.5
n=8
sum=0
for i in range(n+1):
    if i>0:
        sum+=a**i
print(sum)
num=10
sum=0
for i in range(num+1):
    if i>0:
        sum+=1/i
print(sum)
