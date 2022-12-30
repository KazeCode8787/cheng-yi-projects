# v,n = map(int,input().split())    # x=input().split()
# # b=10
# # c=0
# # v=int(x[0])
# # n=int(x[1])

# for a in range(v,n+1):
#     b = 10      
#     c = 0
#     j = len(str(a))
#     at = a
#     while a>0:      #     while a//b>0:
#         d=a%b       #         d=a%b
#         e=d**j      #         e=d**4
#         c=c+e       #         c=c+e
#         a//=10      #         b=10*b
#     if c==at:       #         if c==a:
#         print(at)   #             print(a)



v,n=map(int,input().split())    # x=input().split()


for a in range(v,n+1):
    b=10
    c=0
    while a//b>0:
        d=a%b
        e=d**4
        c=c+e
        b=10*b
    if c==a:       
        print(a)   


