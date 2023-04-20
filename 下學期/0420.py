try:
    x = eval(input("請輸入被除數X:"))
    Y = eval(input("請輸入除數Y:"))
    z = x/Y
except ZeroDivisionError:
    print("除數不得為零")
except Exception as e1:
    print(e1.args)
else:
    print("沒有捕捉到例外!x除以Y的結果等於",z)
finally:
    print("Leaving try...except scope.")