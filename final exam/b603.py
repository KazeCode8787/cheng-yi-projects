x1,y1,x2,y2 = map(int,input().split())

# y2 = a(x2-x1)^2 + y1

a = (y2-y1)/(x2 - x1)**2
if a != int(a):
    a*=(x2 - x1)**2
    k = (x2 - x1)
else:
    k=1
# y*k = a/k(x-x1)**2 + y1

print(f"{k}y = {a/k}x^2+{-1*2*x1*a/k}x+{((a*x1**2)/k+y1*k)}")
