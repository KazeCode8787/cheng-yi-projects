# How to use this class?
A: 
First of all, create files like this:

* Folder-
    * -folder2
        * -something.py
        * -check.py
        * ...
    * -checkpoints
        * -checkpoint1.txt

You can rename anything but checkpoints(dir) and check.py
(checkpoint.txt has to be `checkpoint`+`fileEndingName`+`.txt`)<br>
Inside txt file, enter your input value.

After doing those above, add this to your program:
```
from check import check     #import this module
check(fileEndingName).randoms(min,max,.....)    #This is for creating random check points. You can delete it if you want to
a = check(fileEndingName).read()  
def input() -> str:
    return next(a)
```
Then you can use `input()` function like before but you dont need to enter value by yourself!


# 如何使用這個插件？
A：
首先，依照這個格式創建檔案：

* 文件夾-
    * -文件夾2
        * -something.py
        * -check.py
        * ...
    * -checkpoints
        * -checkpoint1.txt

您可以重命名除了 checkpoints(dir) 和 check.py 之外的任何檔案
（checkpoint.txt 必須是 `checkpoint`+`fileEndingName`+`.txt`）<br>
接著在txt文件裡面輸入您的預設輸入值(測資)。

完成上述操作後，將下列程式碼添加到您的程式中：
```
from check import check #import這個模塊
check(fileEndingName).randoms(min,max,.....) #這是用於創建隨機測資。如果你不想要這個，你可以刪除它
a = check(fileEndingName).read()
def input() -> str:
    return next(a)
```
然後你可以像以前一樣使用`input()`函數，但你不需要自己輸入值！
