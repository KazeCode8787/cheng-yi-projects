class circle:
    PI = 3.14
    radius = 1
    def getArea(self):
        return self.PI*self.radius*self.radius


c1 = circle()
print("半徑為",c1.radius,"的圓面積為",c1.getArea())

c2 = c1
c2.radius = 10
print("半徑為",c2.radius,"的圓面積為",c2.getArea())

class circle:
    PI = 3.14
    def __init__(self,r=1):
        self.radius = r

    def getArea(self):
        return self.PI * self.radius * self.radius

c1 = circle()
print("半徑為",c1.radius,"的圓面積為",c1.getArea())

c2 = circle(10)
print("半徑為",c2.radius,"的圓面積為",c2.getArea())