import random

class check:

    def __init__(self,num:str) -> None:
        self.path = f"./checkpoints/checkpoint{num}.txt"
        #assert True
        pass

    def read(self) -> str:
        with open(self.path,'r',encoding="UTF-8") as file:
            for i in file.readlines():
                yield i.replace('\n','')

    

    def randoms(self,min:int,max:int,amount:int,*,sep:str=' ',prefix:str='') -> None:
        ret = prefix
        for _ in range(amount):
            a = random.randint(min,max)
            ret += str(a) + sep
        
        with open(self.path,'w',encoding="UTF-8") as f:
            f.write(ret)
        return
        
