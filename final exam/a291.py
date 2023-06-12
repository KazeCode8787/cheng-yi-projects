# nAnB
try:
    while True:
    
        password = list(map(int,input().split()))
        times = int(input())
        A = 0
        backip = password.copy()

        for _ in range(times):
            password = backip.copy()
            A = 0
            answer = list(map(int,input().split()))
            # print(answer)
            ansDic = {}
            guessDic = {}

            for i in range(len(answer)):
                if answer[i] == password[i]:
                    answer[i] = -1
                    password[i] = -1
                    A += 1

            for i in range(len(answer)):
                if answer[i] == -1:
                    continue

                try:
                    guessDic[answer[i]] += 1
                except:
                    guessDic[answer[i]]  = 1

            for i in range(len(password)):
                if password[i] == -1:
                    continue

                try:
                    ansDic[password[i]] += 1
                except:
                    ansDic[password[i]]  = 1
            B = 0
            for key in ansDic:
                try:
                    if ansDic[key] == guessDic[key]:
                        B+=1
                except:
                    pass

            print(f"{A}A{B}B")
        input()
except:
    pass