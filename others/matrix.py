from typing import Self

class matrix:
    def __init__(self,data:list,row:int=None,col:int=None) -> None:
        if not (row and col):
            col = len(data[0])
            row = len(data)
        self.row = row
        self.col = col
        if data:
            self.__data = data
        else:
            self.__data = [[0]*col for _ in range(row)]

    def __getitem__(self,index:int):
        return self.__data[index]
    
    def __setitem__(self,index:int,val:int):
        self.__data[index] = val

    def __iter__(self):
        for i_ in range(self.row):
            for j_ in range(self.col):
                yield self.__data[i_][j_]
    
    def __add__(self,target:Self):
        if target.row == self.row and target.col == self.col:
            for i in range(self.row):
                for j in range(self.col):
                    self[i][j] += target[i][j]

        else:
            raise BaseException()
        
        return self
    
    def __sub__(self,target:Self):
        if target.row == self.row and target.col == self.col:
            for i in range(self.row):
                for j in range(self.col):
                    self[i][j] -= target[i][j]

        else:
            raise BaseException()
        
        return self
        
    
    def __mul__(self,target:Self):
        if type(target) == int:
            for i in range(self.row):
                for j in range(self.col):
                    self[i][j] *= target
            return self
        a,b,b2,c = [self.row,self.col,target.row,target.col]
        if b != b2:
            raise BaseException()
        temp = matrix(None,a,c)

        for i in range(a):
            for j in range(c):
                for k in range(b):
                    temp[i][j] += self[i][k]*target[k][j]

        return temp
    
    def __rmul__(self,target:Self):
        if type(target) == int:
                for i in range(self.row):
                    for j in range(self.col):
                        self[i][j] *= target
                return self
        a,b,b2,c = [self.row,self.col,target.row,target.col]
        if b != b2:
            raise BaseException()
        temp = matrix(None,a,c)

        for i in range(a):
            for j in range(c):
                for k in range(b):
                    temp[i][j] += self[i][k]*target[k][j]

        return temp
    
