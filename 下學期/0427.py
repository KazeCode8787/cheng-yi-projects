class circle:
    PI = 3.14

    def __init__(self,r=1) -> None:
        self.radius = r

    def getArea(self):
        return self.PI*self.radius*self.radius


print(f"半徑為 {circle().radius} 的圓面積為 {circle().getArea()}")
print(f"半徑為 {circle(10).radius} 的圓面積為 {circle(10).getArea()}")

class circle:
    PI = 3.14

    def __init__(self,r=1) -> None:
        self.__radius = r

    def getRadius(self):
        return self.__radius

    def getArea(self):
        return self.PI*self.__radius*self.__radius


C1 = circle(10)
print(f"C1的半徑為 {C1.getRadius()}")
print(f"C1的面積為 {C1.getArea()}")

class employee:
    def __init__(self,name) -> None:
        self.__name = name


    def getName(self):
        return self.__name

    def setSalary(self,basic,bonus=0):
        self.__salary = basic+bonus

    def getSalary(self):
        return self.__salary


e1 = employee("ABC")
e2 = employee("DEF")

e1.setSalary(28000)
e2.setSalary(28000,1500)

print(f"員工 {e1.getName()} 的薪水為 {e1.getSalary()}")
print(f"員工 {e2.getName()} 的薪水為 {e2.getSalary()}")
