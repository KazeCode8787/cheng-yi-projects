import csv
import numpy as np
import matplotlib.pyplot as plt
from csv import reader

print("initializing...")
score = {
    "非常不同意":-2,
    "不同意":-1,
    "同意":1,
    "非常同意":2
}

cities = {
    "新北市":{'brightness':0,'wind':0,'space':0,'chair':0,'noise':0,'cold':0,'better':0,'satisfy':0,'count':0},
    "台北市":{'brightness':0,'wind':0,'space':0,'chair':0,'noise':0,'cold':0,'better':0,'satisfy':0,'count':0},
    "基隆市":{'brightness':0,'wind':0,'space':0,'chair':0,'noise':0,'cold':0,'better':0,'satisfy':0,'count':0},
    "桃園市":{'brightness':0,'wind':0,'space':0,'chair':0,'noise':0,'cold':0,'better':0,'satisfy':0,'count':0},
    "新竹縣(市)":{'brightness':0,'wind':0,'space':0,'chair':0,'noise':0,'cold':0,'better':0,'satisfy':0,'count':0},
    "苗栗縣":{'brightness':0,'wind':0,'space':0,'chair':0,'noise':0,'cold':0,'better':0,'satisfy':0,'count':0},
    "台中市":{'brightness':0,'wind':0,'space':0,'chair':0,'noise':0,'cold':0,'better':0,'satisfy':0,'count':0},
    "彰化縣":{'brightness':0,'wind':0,'space':0,'chair':0,'noise':0,'cold':0,'better':0,'satisfy':0,'count':0},
    "南投縣":{'brightness':0,'wind':0,'space':0,'chair':0,'noise':0,'cold':0,'better':0,'satisfy':0,'count':0},
    "雲林縣":{'brightness':0,'wind':0,'space':0,'chair':0,'noise':0,'cold':0,'better':0,'satisfy':0,'count':0},
    "嘉義縣(市)":{'brightness':0,'wind':0,'space':0,'chair':0,'noise':0,'cold':0,'better':0,'satisfy':0,'count':0},
    "台南市":{'brightness':0,'wind':0,'space':0,'chair':0,'noise':0,'cold':0,'better':0,'satisfy':0,'count':0},
    "高雄市":{'brightness':0,'wind':0,'space':0,'chair':0,'noise':0,'cold':0,'better':0,'satisfy':0,'count':0},
    "屏東縣":{'brightness':0,'wind':0,'space':0,'chair':0,'noise':0,'cold':0,'better':0,'satisfy':0,'count':0},
    "台東縣":{'brightness':0,'wind':0,'space':0,'chair':0,'noise':0,'cold':0,'better':0,'satisfy':0,'count':0},
    "花蓮縣":{'brightness':0,'wind':0,'space':0,'chair':0,'noise':0,'cold':0,'better':0,'satisfy':0,'count':0},
    "宜蘭縣":{'brightness':0,'wind':0,'space':0,'chair':0,'noise':0,'cold':0,'better':0,'satisfy':0,'count':0},
    "澎湖縣":{'brightness':0,'wind':0,'space':0,'chair':0,'noise':0,'cold':0,'better':0,'satisfy':0,'count':0},
    "連江縣":{'brightness':0,'wind':0,'space':0,'chair':0,'noise':0,'cold':0,'better':0,'satisfy':0,'count':0},
    "金門縣":{'brightness':0,'wind':0,'space':0,'chair':0,'noise':0,'cold':0,'better':0,'satisfy':0,'count':0},
}

traslate = {
    "新北市":"New Taipei",
    "台北市":"Taipei",
    "基隆市":"Keelung",
    "桃園市":"Taoyuan",
    "新竹縣(市)":"Hsinchu",
    "苗栗縣":"Miaoli",
    "台中市":"Taichung",
    "彰化縣":"Changhua",
    "南投縣":"Nantou",
    "雲林縣":"Yunlin",
    "嘉義縣(市)":"Chiayi",
    "台南市":"Tainan",
    "高雄市":"Kaohsiung",
    "屏東縣":"Pingtung",
    "台東縣":"Taitung",
    "花蓮縣":"Hualien",
    "宜蘭縣":"Yilan",
    "澎湖縣":"Penghu",
    "連江縣":"Lianjiang",
    "金門縣":"Jinmen",
}

people = {
    "less_than_10":0,
    "10_to_20":0,
    "20_to_30":0,
    "30_to_40":0,
    "more_than_40":0
}

Sum = 0
mainQuestion = ('brightness','wind','space','chair','noise','cold','better','satisfy','count')
print("reading file...")
csvfile = open('./data.csv','r',encoding='utf-8')
file = csv.reader(csvfile)     # 讀取 csv 檔案
data = tuple(file)
print("file has been read!")

''' data index
[
    '時間戳記',
    '請問您目前就讀的學校是?(可不輸入學校名稱，如XX高中)',
    '請問貴班有幾人',
    '請問您就讀的學校位於哪個縣市',
    '請回答下列問題 [我認為教室明亮度是足夠的]', 
    '請回答下列問題 [我認為教室通風度是足夠的]', 
    '請回答下列問題 [我認為教室的空間是足夠的]', 
    '請回答下列問題 [我認為椅子坐起來是舒服的]', 
    '請回答下列問題 [我認為來自課程外的聲響不會影響學習]', 
    '請回答下列問題 [我認為冷氣可以使學習環境更舒適]',
    '請回答下列問題 [我認為學習環境還可以更好]',
    '你對於現今的學習環境滿意度為'
]
'''
print("Scanning...")
for i in range(len(data)):         # 將讀取的檔案，轉換成串列的方式，印出每個項目
    if i == 0:
        continue

    temp = tuple(map(lambda v:score[v],data[i][4:-1]))
    # 4 5 6 7 8 9 10 all bad
    if sum(temp) < -12 or sum(temp) > 12:
        print("Error! All completely (dis)agree!")
        print(data[i])
        if input("Save(y) or Skip(n)?") == "n":
            continue


    # data[i][3] is the city of the school
    # adding answers to specific
    for j in range(len(temp)):
        cities[data[i][3]][mainQuestion[j]] += temp[j]
    Sum += 1
    cities[data[i][3]]['count'] += 1

    # data[i][2] is the student amount of the class
    classMates = int(data[i][2])
    if classMates < 10:
        people['less_than_10'] += 1
    elif classMates < 20:   #10~19
        people['10_to_20'] += 1
    elif classMates < 30:   #20~29
        people['20_to_30'] += 1
    elif classMates < 40:   #30~39
        people['30_to_40'] += 1
    else:                   #40++
        people['more_than_40'] += 1

    totalSatisfy = int(data[i][11])
    cities[data[i][3]]['satisfy'] += totalSatisfy

# Delete useless cities
pops = []
for i in cities:
    if cities[i]['count'] == 0:
        pops.append(i)

for i in pops:
    cities.pop(i)

# Average
for city in cities:
    for element in cities[city]:
        if element != 'count':
            cities[city][element] /= cities[city]['count']

print("Finish!")

# making charts
x = np.array([traslate[i] for i in sorted(cities,key=lambda v:cities[v]['satisfy'],reverse=True)])
y = list(map(lambda v:v['satisfy'],list(cities.values())))
y.sort(reverse=True)
y = np.array(y)
# new_key,new_val = temp.keys(),temp.values()


plt.bar(x,y)
plt.show()