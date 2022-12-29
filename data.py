class stack:

    def __init__(self,*args) -> None:
        self.__stack = list(args)


    def __len__(self) -> int:
        return len(self.__stack)


    def __str__(self) -> str:
        return f"{self.__stack[::-1]}"


    def __iter__(self):
        for i in self.__stack[::-1]:
            yield i

    
    def __getitem__(self,index):
        return self.__stack[::-1][index]


    def push(self,*args) -> None:
        if len(args)==1:
            self.__stack.append(args[0])
            return None
        else:
            for i in args:
                self.__stack.append(i)
            return None


    def pop(self) -> any:
        return self.__stack.pop(-1)
        


class queue:

    def __init__(self,*args) -> None:
        self.__queue = list(args)

    
    def __len__(self) -> int:
        return len(self.__stack)


    def __str__(self) -> str:
        return f"{self.__queue}"

    
    def __iter__(self):
        for i in self.__queue:
            yield i


    def __getitem__(self,index):
        return self.__queue[index]

    
    def inqueue(self,*args) -> None:
        if len(args)==1:
            self.__queue.append(args[0])
            return None
        else:
            for i in args:
                self.__queue.append(i)
            return None


    def dequeue(self) -> any:
        return self.__queue.pop(0)



