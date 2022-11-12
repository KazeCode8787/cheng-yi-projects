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
