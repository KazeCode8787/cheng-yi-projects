print(0o101)
print(0x41)
print(-0x41)
print(1<2)
print(1>2)
print(type(1000))
print(type(-12.53))
print(type(2+1j))
print(type(True))
print(type(False))
print(type("Pa"))
print(type('p'))
print(12+30)
print(1.234+5.678)
print(12-3)
print(1.456-5.456)
print(12*3)
print(10*0.5)
print(12/3)
print(1/3)
print(12//3)
print(8//3)
print(12%5)
print(9**2)
print(9**0.5)
print(2/3.0)
print(12.3*10%5)
print(123//5)
print("A"=="a")
print((5>3)or(4<2))
print((5<=9)and(not(3>7)))
print(10*2=="20")
print("Wow"*4)
print(("abc"!="ABC")or(3>5))
print("8"+"Happy")
print(-128>>3)
print(2<<10)
print(2&10)
print(2|10)
score1 = eval(input("國文分數："))
score2 = eval(input("英文分數："))
score3 = eval(input("數學分數："))

total = score1 + score2 + score3
print("總成績為：",total)

top = eval(input("上底："))
btn = eval(input("下底："))
hig = eval(input("高："))

area = (top+btn)*hig/2
print("面積為：",area)

x1,y1 = eval(input("第一個點"))
x2,y2 = eval(input("第二個點"))

dis = ((x2-x1)**2+(y2-y1)**2)**0.5
print("兩點距離",dis)
print((-5+(5**2-4*2*2)**0.5)/(2*2))
print((100**2-50**2)/(100+50))