array = [54,2,40,22,17,22,60,35]
try:
    a = array.index(22)
    print(f"找到值等於22的資料，其索引為{a}")
except:
    print(-1)

array2 = [[1,2,3],[4,5,6],[7,8,9],[10,11,12]]
sum2 = 0
for sa in array2:
    sum2 += sum(sa)

print(sum2)

string = input()

for i in string[::-1]:
    print(i)