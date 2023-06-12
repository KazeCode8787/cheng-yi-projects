# 眾數

N = int(input())
nums = list(map(int,input().split()))

counts = {}

for n in nums:
    if not counts.get(n):
        counts[n] = 1
    else:
        counts[n] += 1

x = sorted(counts)
maxs = []
max_ = -1
for i in x:
    if counts[i] >= max_:
        max_ = counts[i]
        print(i,counts[i])
        continue
    break

# print(counts)