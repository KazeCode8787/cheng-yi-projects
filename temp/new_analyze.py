import csv

class analyze:

    # 讀取 csv 檔案
    def __init__(self) -> None:
        csvfile = open('./data.csv','r',encoding='utf-8')
        file = csv.reader(csvfile)
        self.__data = tuple(file)
        self.__keys = ('school','students','city','brightness','wind','space','chair','noise','cold','better','satisfy','count')
        self.__score = {
            "非常不同意":-2,
            "不同意":-1,
            "同意":1,
            "非常同意":2
        }
    
    # 中位數
    def median(self,*,city=None,target=None) -> int:
        assert target in self.__keys  # check if target exists
        if target == "satisfy":
            return self.__sa_med(city=city)

        targetId = self.__keys.index(target)
        data = self.__data
        temp = []
        if city:    #依照城市搜索
            for i in range(1,len(data)):
                a = tuple(map(lambda v:self.__score[v],data[i][4:-1]))
                if sum(a) <= -14 or sum(a) >= 14:
                    continue
                if data[i][3] != city:
                    continue
                temp.append(int(a[targetId-3]))
        else:   #沒提供城市
            for i in range(1,len(data)):
                a = tuple(map(lambda v:self.__score[v],data[i][4:-1]))
                if sum(a) <= -14 or sum(a) >= 14:
                    continue
                temp.append(int(a[targetId-3]))
        temp.sort()
        return int(temp[len(temp)//2])
        
    # 眾數
    def mode(self,*,city=None,target=None) -> int:
        assert target in self.__keys  # check if target exists
        if target == "satisfy":
            return self.__sa_mod(city=city)

        targetId = self.__keys.index(target)
        data = self.__data
        s_temp = set()
        temp = []
        if city:    #依照城市搜索
            for i in range(1,len(data)):
                if data[i][3] != city:
                    continue
                a = tuple(map(lambda v:self.__score[v],data[i][4:-1]))
                if sum(a) <= -14 or sum(a) >= 14:
                    continue
                temp.append(int(a[targetId-3]))
                s_temp.add(int(a[targetId-3]))
        else:   #沒提供城市
            for i in range(1,len(data)):
                a = tuple(map(lambda v:self.__score[v],data[i][4:-1]))
                if sum(a) <= -14 or sum(a) >= 14:
                    continue
                temp.append(int(a[targetId-3]))
                s_temp.add(int(a[targetId-3]))
        s_temp = list(s_temp)
        s_temp.sort(key=lambda v:temp.count(v),reverse=True)
        return int(s_temp[0])

    # 算術平均數
    def average(self,*,city=None,target=None) -> int:
        assert target in self.__keys  # check if target exists
        if target == "satisfy":
            return self.__sa_aver(city=city)

        targetId = self.__keys.index(target)
        data = self.__data
        count = 0
        Sum = 0
        if city:    #依照城市搜索
            for i in range(1,len(data)):
                if data[i][3] != city:
                    continue
                a = tuple(map(lambda v:self.__score[v],data[i][4:-1]))
                if sum(a) <= -14 or sum(a) >= 14:
                    print(data[i])
                    continue
                Sum += int(a[targetId-3])
                count += 1
        else:   #沒提供城市
            for i in range(1,len(data)):
                a = tuple(map(lambda v:self.__score[v],data[i][4:-1]))
                if sum(a) <= -14 or sum(a) >= 14:
                    continue
                Sum += int(a[targetId-3])
                count += 1
        assert count > 0
        return  (Sum/count)

    # 人數
    def people(self,*,amount=None):
        assert amount>0
        data = self.__data
        for i in range(1,len(data)):
            if int(data[i][2]) == amount:
                print(data[i])

    # 城鄉差距
    def cityDif(self,*,target=None) -> tuple:
        assert target in self.__keys  # check if target exists
        if target == "satisfy":
            return self.__sa_CD()
        data = self.__data
        targetId = self.__keys.index(target)
        cc = 0
        oc = 0
        capitals = 0
        others = 0
        for i in range(1,len(data)):
            if data[i][3] in ("新北市","台北市","桃園市","台中市","台南市","高雄市"):
                a = tuple(map(lambda v:self.__score[v],data[i][4:-1]))
                capitals += int(a[targetId-3])
                cc += 1
            else:
                a = tuple(map(lambda v:self.__score[v],data[i][4:-1]))
                others += int(a[targetId-3])
                oc += 1
        return (capitals/cc,others/oc)
                

    # 滿意度中位數
    def __sa_med(self,*,city=None) -> int:
        data = self.__data
        temp = []
        if city:    # 依照城市搜索
            for i in range(1,len(data)):
                if data[i][3] != city:
                    continue
                temp.append(int(data[i][-1]))
        else:   # 沒提供城市
            for i in range(1,len(data)):
                temp.append(int(data[i][-1]))
        temp.sort()
        return int(temp[len(temp)//2])

    # 滿意度眾數
    def __sa_mod(self,*,city=None) -> int:
        data = self.__data
        s_temp = set()
        temp = []
        if city:    # 依照城市搜索
            for i in range(1,len(data)):
                if data[i][3] != city:
                    continue
                temp.append(int(data[i][-1]))
                s_temp.add(int(data[i][-1]))
        else:   # 沒提供城市
            for i in range(1,len(data)):
                temp.append(int(data[i][-1]))
                s_temp.add(int(data[i][-1]))
        s_temp = list(s_temp)
        s_temp.sort(key=lambda v:temp.count(v),reverse=True)
        return int(s_temp[0])

    # 滿意度平均
    def __sa_aver(self,*,city=None) -> int:
        data = self.__data
        count = 0
        Sum = 0
        if city:    # 依照城市搜索
            for i in range(1,len(data)):
                if data[i][3] != city:
                    continue
                Sum += int(data[i][-1])
                count += 1
        else:   # 沒提供城市
            for i in range(1,len(data)):
                Sum += int(data[i][-1])
                count += 1
        assert count > 0
        return  (Sum/count)

    # 滿意度城鄉差距
    def __sa_CD(self) -> tuple:
        data = self.__data
        capitals = 0
        others = 0
        oc = 0
        cc = 0
        for i in range(1,len(data)):
            if data[i][3] in ("新北市","台北市","桃園市","台中市","台南市","高雄市"):
                capitals += int(data[i][-1])
                cc += 1
            else:
                others += int(data[i][-1])
                oc += 1
        return (capitals/cc,others/oc)

    
