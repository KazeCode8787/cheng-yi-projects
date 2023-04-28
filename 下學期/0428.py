class A:
    x=1

class B(A):
    y=2

class C(B):
    z=3





obj = C()
print(f"x的屬性值為 {obj.x}")
print(f"y的屬性值為 {obj.y}")
print(f"z的屬性值為 {obj.z}")

# class A:
#     x = 
class B:
    y = 2

class C(A,B):
    z = 3

obj = C()
print(f"x的屬性值為 {obj.x}")
print(f"y的屬性值為 {obj.y}")
print(f"z的屬性值為 {obj.z}")

class shoppingcar():
    def __init__(self,owner) -> None:
        self.__owner = owner
        self.__product = []

    def getOwner(self):
        return self.__owner

    def addProduct(self,product):
        self.__product.append(product)
        # return self

    def removeProduct(self,product):
        self.__product.remove(product)
        # return self

    def getProduct(self):
        return self.__product


obj = shoppingcar("dogg")

obj.addProduct("abc")
obj.addProduct("sss")
obj.addProduct("aaa")
obj.addProduct("www")
obj.addProduct("qqq")
obj.addProduct("sdsd")
obj.removeProduct("abc")
print(f"{obj.getOwner()} 的購物車內有 {obj.getProduct()}")