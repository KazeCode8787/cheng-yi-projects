a = [[1,2,3],[4,5,6],[7,8,9]]



def show(matrix):    
    for i in range(len(matrix)):
        tp = list(map(str,matrix[i]))
        print("\t".join(tp))

b = []


show(a)
print("------------------------")


for i in range(len(a)):
    b.append([])
    for j in range(len(a)):
        b[i].append(a[j][i])


show(b)
ctn = 0

for i in range(len(a)):
    ctn += sum(a[i])

print(ctn)