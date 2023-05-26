class matrix:
    def __init__(self,col:int,row:int,*,data=None) -> None:
        self.col = col
        self.row = row
        if data:
            self.__data = data
        else:
            self.__data = [[0]*row for _ in range(col)]

    def __getitem__(self,index):
        return self.__data[index]
    
    def __add__(self,target):
        if target.col == self.col and target.row == self.row:
            for i in range(self.col):
                for j in range(self.row):
                    self[i][j] += target[i][j]

        else:
            raise BaseException()
        
        return self
    
    def __sub__(self,target):
        if target.col == self.col and target.row == self.row:
            for i in range(self.col):
                for j in range(self.row):
                    self[i][j] -= target[i][j]

        else:
            raise BaseException()
        
        return self
        
    
    def __mul__(self,target):
        if type(target) == int:
            for i in range(self.col):
                for j in range(self.row):
                    self[i][j] *= target
            return self
        a,b,b2,c = [self.col,self.row,target.col,target.row]
        if b != b2:
            raise BaseException()
        temp = matrix(a,c)

        for i in range(a):
            for j in range(c):
                for k in range(b):
                    temp[i][j] += self[i][k]*target[k][j]

        return temp
    
    def __rmul__(self,target):
        if type(target) == int:
                for i in range(self.col):
                    for j in range(self.row):
                        self[i][j] *= target
                return self
        a,b,b2,c = [self.col,self.row,target.col,target.row]
        if b != b2:
            raise BaseException()
        temp = matrix(a,c)

        for i in range(a):
            for j in range(c):
                for k in range(b):
                    temp[i][j] += self[i][k]*target[k][j]

        return temp
    def __setitem__(self,index,val):
        self.__data[index] = val

    def __iter__(self):
        for i_ in range(self.col):
            for j_ in range(self.row):
                yield self.__data[i_][j_]
