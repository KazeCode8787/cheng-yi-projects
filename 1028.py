top, bottom, height = 10, 20, 5
print("梯形的上底{}cm, 下底{}cm, 高{}cm".format(top,bottom,height))
s1 = "\nMerry\tChristmas!\n"
print(s1.strip())
print(s1)
s4 = "Monday"
s5 = "monday"
print(s4.center(30))
s6 = s4.upper()
print(s6)
s7 = s4.lower()
print(s7)
s8 = s5.replace("mon","Fri")
print(s4.isdigit())
print(s4.endswith('day'))
print(s4.find('o'))
print(format(123,"<10"))
print(format(123,">10"))
print(format(123,"^10"))
print(format(123,"$^10"))
print(format(123456789,","))
print(format(65,"#b"))
print(format(65,"#o"))
print(format(65,"#x"))
print(format(123,"=+010"))
print(format(1234.5678,"10.2f"))
print(format(1234.5678,"10.2e"))
print(format(12,"10.2e"))
print(format(8,"10.2%"))
print(format(7654.321,"<15.2f"))
print(format(7654.321,"^15,.2f"))
print(format("Hi, Siri!","20"))
print(format("Hi, Siri!",">20"))
print(format("Hi, Siri!","^20"))
print(format("Hi, Siri!","5"))
print("{:^10}{:^10}{:^10}".format("年度","營業額","獲利率"))
print("{:^12}{:^12}{:^14.2%}".format("108",1550000,0.0309))
print("{:^12}{:^12}{:^14.2%}".format("109",2000000,0.0523))
print("{:^12}{:^12}{:^14.2%}".format("110",2234000,0.0547))

s1 = "Today is Friday"
print("day" in s1)
print(s1.count("day"))
print(s1.find("day"))
print(s1.rfind("day"))
new1 = s1.replace("Friday","Saturday")
new2 = s1.swapcase()
print(new1)
print(new2)
print(s1.isupper())
print(f"{s1:>20}")
print(max(s1))
print(s1[2:5])
a = pow(int(input()),0.5)
print(f'{a:.5f}')
