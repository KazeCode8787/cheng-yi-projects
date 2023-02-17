list1 = [10,20,30,40,50]
list2 = [100,200,300]
list1.append(60)
print(list1)
list1.extend(list2)
print(list1)
list1.insert(1,1000)
print(list1)
list1.remove(1000)
print(list1)
print(list1.pop())
print(list1)

list1 = [50,20,40,20,30,20,10]
print(list1.index(20))

print(list1.count(20))

list1.sort()
print(list1)
list1.reverse()
print(list1)
list2 = list1.copy()
print(list2)
list2.clear()
print(list2)
