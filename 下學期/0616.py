# 眾數

N = int(input())
nums = list(map(int,input().split()))

counts = {}

for n in nums:
    if not counts.get(n):
        counts[n] = 1
    else:
        counts[n] += 1
        
for i in counts:
    print(f"{i}:{counts[i]}")