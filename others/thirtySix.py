class thirtySix:

    def __init__(self,val,type=None):
        if not type:
            if '0b' in val:
                self.__type = 2
                val = val[2:]
            elif '0x' in val:
                self.__type = 16
                val = val[2:]
            elif '0o' in val:
                self.__type = 8
                val = val[2:]
            elif '0t' in val:
                self.__type = 36
                val = val[2:]
            else:
                self.__type = 10
        else:
            self.__type = type
        self.__value = 0
        if self.__type == 36:
            for i in range(len(val)):
                if val[i].isalpha():
                    self.__value += (ord(val[i])-55)*(36**(len(val)-1-i))
                else:
                    self.__value += (int(val[i]))*(36**(len(val)-1-i))
            return None
        self.__value = int(str(val),self.__type)
        
        

    def toDec(self):
        return self.__value

    def toHex(self):
        return hex(self.__value)

    def toBin(self):
        return bin(self.__value)

    def toOct(self):
        return oct(self.__value)

    def toTS(self):
        __v = self.__value
        __final = []
        while __v >= 36:
            temp = __v % 36
            __v //= 36
            if temp > 9:
                temp = chr(65+temp-10)
            __final.append(temp)
        if __v > 9:
            __v = chr(65+__v-10)
        __final.append(__v)
        
        return "0t"+"".join(map(str,__final[::-1]))
