class matrix:
    def __init__(self,col:int,row:int,*,data=None) -> None:
        self.col = col
        self.row = row
        if data:
            self.__data = data
        else:
            self.__data = [[0]*row for _ in range(col)]

            