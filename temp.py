import csv
from csv import reader

csvfile = open('./abc.csv')
r = csv.reader(csvfile)     # 讀取 csv 檔案
r = tuple(r)
for i in range(len(r)):         # 將讀取的檔案，轉換成串列的方式，印出每個項目
    if i == 0:
        continue
    print(r[i])