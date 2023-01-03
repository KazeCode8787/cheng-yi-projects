# cheng-yi-projects

## [0902-1.py](https://github.com/KazeCode8787/cheng-yi-projects/blob/main/0902-1.py)
### Topic: print()
呼叫 print() 來顯示資料
* ()內可輸入各種資料型態，如：
	* 字串型態 `print("abcdefg123")`
	* 整數、浮點數(含小數點) `print(1)` `print(3.14)`
		* ()內也可做計算 `print(1+1)`
		* 計算時 __先乘除後加減，括號優先__
	* 布林值(成立/不成立:True/False) `print(True)`
	* (以上未列舉所有型態)
	
* ()內可將兩種相同或不同型態的資料結合，如：
	* 相同
		* **字串+字串** `print("a"+"b")` 結果："ab"
		* **字串,字串** `print("a","b")` 結果："a b"
	* 不同
		* **字串,數字** `print("a",2+3,3)` 結果："a 5 3"
---
## [0916.py](https://github.com/KazeCode8787/cheng-yi-projects/blob/main/0916.py)
### Topic: data type(資料型態)
#### 主要資料型態
* int
	* 整數型態(`0`,`123456`,`-4564`)
	* **沒有**小數點

* float
	* 浮點數型態(`1.0`,`-2.3`,`1234.567`,`float("inf")`)
	* 含**小數點**的數字

* str
	* 字串型態(以雙括弧`" "`或單括弧`' '`包圍)
	* 文字，**不可運算**

* bool
	* 布林值型態(`true`,`false`)
	* 用於**比較是、否**

而其他資料型態如虛數不常使用，便不於此處提及
#### 進階資料型態
* list, tuple, set
	* 三者皆為**類似串列**的資料，可儲存多筆資料

* list(串列、陣列)
	* 以`[]`包覆資料，資料間以`,`分隔
	* 資料可以是各種**不同的型態**如`[0,"0",true,[0,1,2]]`
	*說明：上述陣列資料型態分別為：*
	`[整數,字串,布林值,陣列]`
	* 類似於C++的array(陣列)
	* 第一項**索引值**為**0**，第二項為1...
	* 讀取myList中第n項方式：`myList[n]`
	* 宣告方式：`myList = []`
* tuple(元組)
	* 以`()`包覆資料，資料間以`,`分隔
	* 資料可以是各種**不同的型態**如`(0,"0",true,(0,1,2))`
	*說明：上述元組資料型態分別為：*
	`(整數,字串,布林值,元組)`
	* 類似於上方list，但python讀取tuple**速度較list快**，且tuple**不可被修改**
	* 第一項**索引值**為**0**，第二項為1...
	* 讀取myTuple中第n項方式：`myTuple[n]`
	* 宣告方式：`myTuple = ()`
* set(集合)
	* 以`{}`包覆資料，資料間以`,`分隔
	* 資料可以是各種**不同的型態**如`{0,"0",true,(0,1,2)}`
	*說明：上述集合資料型態分別為：*
	`{整數,字串,布林值,元組}`
	* 類似於上方list，但set**不會有重複的資料**，且會**自動排序**
	* 第一項**索引值**為**0**，第二項為1...
	* 讀取mySet中第n項方式：`mySet[n]` **才怪**
	* 集合不可直接讀取，需使用for迴圈
	* 集合有特殊的邏輯運算子：交集`&` 聯集`|` 非交集`^` 差集`A-B`等
	* 宣告方式：`mySet = set()` `mySet = {0,"0",true,(0,1,2)}`

* dict(字典)
	* 以`{}`包覆資料，資料間以`,`分隔
	* 每筆資料皆為`key:value`的型態(`索引值:值`)
	* key只能是**字串型態**
	* value可以是各種**不同的型態**
	* 讀取myList中`"a"`的方式：`myDict["a"]`
	* 宣告方式：`myDict = {}`
	* 更改第`"wtf"`項方式：`myDict["wtf"] = "sus"`

##### 重點整理
把這些資料想像成一本字典 *(並非上方dict)*，`list,tuple`為頁碼查詢，而資料排序**毫無規則**；`set`為筆畫查詢，越後面**筆畫越多**；`dict`為字音查詢，**只會查詢到一樣物品**

### Topic: Operators(運算子)
對於一筆以上的資料進行運算的符號
* **加減乘除(五則運算)**
	* 先乘除後加減，括號內先運算，其他從左至右讀入
	例如

	 算式| 結果
	 :-----: | ----------:
	 (4*(5+3))/2+5  | 21
	 (4*(5+3))/(2+5) | 4.57

* 特殊運算(整數除法`//`、餘數`%`)
	
	 算式| 結果
	 :-----: | ----------:
	 5/3 | 1.66666666
	 5//3 | **1**
	 5%3 | **2**

* 邏輯運算
	* 邏輯運算子(**T與F的比較**)
		* and[^1], or[^2], not[^3]
	* 位元邏輯運算子(**1與0的比較**)
		* &[^4], |[^5], \^[^6]



* 位元運算
	* 運算過程：**十進位 -> 二進位 -> 位移 -> 十進位**

	 算式| 十進位 | 二進位 |位移 |十進位
	 :-----: | :----------:| :----------:| :----------:| :----------:
	 5<<3 | 5|101|101000|40
	 8>>2 | 8|1000|10|2
	 
### Topic: eval()
將傳入的值轉為運算式
* `eval(3+5)` 輸出**錯誤**
* `eval("3+5")` 輸出8
* `eval("3+5*4+3")` 輸出26
* `eval("1,2")` 輸出(1,2) _類型為tuple_

### Topic: input()
* 括號內填入提示文字
* 回傳必為字串型態

## [0923.py&0930.py](https://github.com/KazeCode8787/cheng-yi-projects/blob/main/0923.py)
[0930.py連結](https://github.com/KazeCode8787/cheng-yi-projects/blob/main/0930.py)
### Topic: math(數學類別)/random(亂數類別)
#### Python 內建數學函式
python 中內建的數學函式有很多，無法一一列舉，這邊只講幾個
* max(),min()
	* 回傳最大/小值
	* 括號內可傳入list,tuple等可迭代資料
* abs()
	* 回傳絕對值
	* 括號內只可傳入數值型態
* hex(),bin(),oct()
	* 回傳16,2,8進位
	* 括號內填入一整數型態
	
#### math 類別
math是python中內建的一個class(類別)，使用時需要import(引用)
* import module as module_name
	* 前面的module是類別名稱，例如`import math`
	* as後方的module_name是未來想要呼叫時的名稱，會較為方便，例如`import math as ma`

math類別中有許多函式，適合用於進階運算，此處不一一列舉，有興趣可參考[這個網站](https://www.w3schools.com/python/module_math.asp)
### Topic: unicode/ascii code
#### unicode/ascii code
為一種特殊編碼模式，可以叫出特殊字元，常在辨識是否為英文字母或數字使用到
使用方式；
* 八進位模式
	* `"\101"`為A
* 十六進位模式
	* `"\x41"`為ascii code的A
	* `"\u0041"`為unicode的A
* 名稱搜尋模式
	* `"\N{BLACK SPADE SUIT}"`可搜尋unicode中的BLACK SPADE SUIT

## [1007.py](https://github.com/KazeCode8787/cheng-yi-projects/blob/main/1007.py)
### Topic: String(字串型態)
可將String想成是一個儲存字元的陣列<br>
每一個index都只對應到一個字元<br>
並且可使用list大多數的方法或函式<br>
也就是說，String算是一個iterable(可迭代資料)

## [1021.py](https://github.com/KazeCode8787/cheng-yi-projects/blob/main/1021.py)
### Topic: String methods(字串方法)
太多了不想講自己看[API](https://www.w3schools.com/python/python_strings_methods.asp)

## [1028.py](https://github.com/KazeCode8787/cheng-yi-projects/blob/main/1028.py)
### Topic: f-String(格式化字串型態)
格式化字串主要有兩種方式
* `"Some String, arg1:{}, arg2:{}".format(arg1,arg2,...)`
	* 此方法需在前方字串預先放入大括弧，為填入的值預留空位
* `f"Some String, arg1:{arg1}, arg2:{arg2}"`
	* 此方法需在字串的引號前加入`f`，並在大括弧內直接填入變數

格式化字串可以排版，只需在大括號內填入`{:^10}`等即可<br>
`^`,`<`,`>` 分別為置中、向左靠、向右靠<br>
後方的數值為預留的空位<br>
需要注意的是，`"".format()`是輸入如`{:^10}`<br>
而`f""`是輸入`{arg:^10}`，冒號要在數值後方<br>
格式化還可以有其他變化，這邊就不多提及<br>

## [1111.py](https://github.com/KazeCode8787/cheng-yi-projects/blob/main/1111.py)
### Topic: if statment
if 可判斷其後方的狀態是否為真(True)，若成立則執行if下方的動作，反之執行else
例如：
```
if 1<2:
    print("Yes")
else:
    print('no')
```
則此程式必輸出`Yes`

因為python沒有提供switch
所以要大量判斷時只能使用elif
elif 是else + if
如果前一個if沒有成立，程式將會自動跳到else
若else後方有if，程式會再度判斷是否成立
例如：
```
if 5<2:
    print('1')
elif 5<6:
    print('2')
else:
    print('3')
```
則此程式輸出`2`

#### 特殊狀況
在沒有給予其他條件時，if視以下狀況為`False`
> 1. None
> 2. 0 (int)
> 3. False
> 4. 空的資料，如`""(空字串)`,`[](空串列)`

例如：
```
if 0:
    print("hi")
else:
    print("no")
```
則此程式必輸出`no`

#### 單行判斷式
此部分可學可不學
不學不影響程式速度
學了看起來更帥
舉例：
```
if 10>7:
    a = 5
else:
    a = 3
```
此程式也可以這樣寫：
`a = 5 if 10>7 else 3`<br>而巢狀判斷也可以用一行來做
舉[1111.py](https://github.com/KazeCode8787/cheng-yi-projects/blob/main/1111.py)的第17行為例
可以改成<br>
`print("優等" if score >= 90 else "甲等" if score < 90 and score >= 80 else "乙等" if score < 80 and score >= 70 else "丙等" if score < 70 and score >= 80 else "不及格")`
很長，也很難讀，但這種用法在`lambda`可能會用到

## [1202.py](https://github.com/KazeCode8787/cheng-yi-projects/blob/main/1202.py)
### Topic: for/while loop
for迴圈與 while迴圈是各個程式語言中最重要的迴圈技巧
使用時機簡單來說，**明確知道**要跑幾次，使用for；反之使用while
例如：
> 明確知道要跑5次，使用for i in range(5)
> 知道要跑到`i>j`但不知道要跑幾次，使用while i<=j

#### for 迴圈
* 用法(python官方提供)
> "for" target_list "in" starred_list ":" suite 

看完火星文，來看看人話
首先，上面所說的`starred_list`即為**可迭代資料**
說簡單點就是list, tuple, set, dict等
當然還有其他的可以拿來迭代，這邊就不提
主要會常用到的有兩種方法
`in range()`或`in list`
* for i in range(start,end,step)
	* range()會產生一個可迭代資料
	* start是起始值(預設為0), end為結束值(但不包含end本身), step是每次迴圈需改變多少(預設為1)
	* 例如：`range(5)` -> `0,1,2,3,4`;`range(1,5)` -> `1,2,3,4`;`range(0,5,2)` -> `0,2,4`
* for i in list
	* 可直接讀出list中的資料
	* list可以是tuple, set, dict等
	* 此時i會是list,tuple,set的值,或是dict的key

同時，for迴圈可加入else
只要for迴圈沒有被主動break掉，便會自動進入else

#### while 迴圈
* 用法(python官方提供)
> "while" assignment_expression ":" suite

看完火星文，來看看人話

首先，上面所說的`assignment_expression`即為**判斷式**<br>
該判斷式需回傳True或False<br>
而當判斷式為True時，執行迴圈<br>
也就是說，`while True`可達成無限循環，而`while False`無意義
而while與if的判斷雷同

同時，while迴圈可加入else
只要while迴圈沒有被主動break掉，便會自動進入else

#### 小技巧
執行迴圈時，有兩個可使用的關鍵字
`break`以及`continue`
* break
	* break會直接打掉迴圈，使迴圈立即結束
* continue
	* continue會結束本次迴圈的執行，並進入下一次的迴圈

兩者最大的差異就是continue還是保留在迴圈內
而break會直接退出迴圈

## [1209.py](https://github.com/KazeCode8787/cheng-yi-projects/blob/main/1209.py)
### Topic: def 自訂函式

def關鍵字可以用來自定義函式(function)
自訂函式的優缺點如下
* 優點
	* 可以快速呼叫需重複執行的指令
	* 維護時較為快速，只需修改定義的地方，不需全部更改
* 缺點
	* 執行時間較長
	* 易有區域及全域變數混淆之情形

#### 用法
```
def plus():
	print("1+1=",2)

plus()
plus()
```

上述程式會輸出兩次`2`<br>
但這個程式目前是比較沒用的，畢竟它裡面只做一件事情而已<br>
所以我們可以把它改成這樣<br>

```
def plus():
	num = int(input("Please enter your number:"))
	print(num+num)

plus()
plus()
```

上述程式可以執行兩次的詢問數值及印出結果<br>
但如果我不想要讓使用者輸入，而是直接傳入不一樣的數值就要用到變數<br>

```
def plus(num):
	print(num+num)

plus(5)
plus(4)
plus()
```

上述程式可以輸出`10`以及`8`<br>
而最後那一行則會報錯，原因很簡單，就只是預設要輸入一個變數，但你只輸入了一個<br>
解決的方法很簡單，只需要先幫num**訂好預設值**就可以了<br>
```
def plus(num=0):
	print(num+num)

plus(5)
plus(4)
plus()
```
上述程式可以輸出`10`以及`8`還有`0`<br>
但如果我想要讓兩個**不同的數值**相加，就要必須用到兩個變數<br>

```
def plus(num1,num2):
	print(num1+num2)

plus(5,1)
plus(4,3)
plus(2,3,4)
```

上述程式可以輸出`6`以及`7`<br>
而最後那一行則會報錯，原因很簡單，就只是預設只能輸入兩個變數，但你卻輸入了三個
解決方式也很簡單，只要更改一夏，加一個符號即可<br>

```
def plus(*nums):
	print(nums)

plus(5,1)
plus(4,3)
plus(2,3,4)
```
這時候你會發現，他印出了`6`,`7`,`9`**才怪**<br>
原因是，使用*符號的變數會以`tuple`的型態儲存<br>
所以他會印出`(5,1)`,`(4,3)`,`(2,3,4)`等資料
所以我們要改一下內部指令
```
def plus(*nums):
	print(sum(nums))

plus(5,1)
plus(4,3)
plus(2,3,4)
```
這樣就可以了<br>
<br>
再來，有些程式會使用到以下變數宣告
```
def minus(*,a,b):
    print(a-b)
```

此時呼叫`minus(2,1)`會輸出 `1` **才有鬼**<br>
應該是要`minus(a=2,b=1)`才行<br>
你問我為什麼? 原因其實很簡單：<br>
若*號後方沒有參數名稱而是逗號，接下來的參數都被稱作**關鍵字引數**<br>
這些參數都必須要用它的名稱來傳入特定的值<br>
如上述，若要傳給`a`一個5，就必須使用`a=5`<br>
值得注意的是關鍵字不需按照原順序傳入，如上可先傳入b再傳入a<br>

那如果我今天想要傳N個關鍵字引數呢?<br>
只需要將指令改成這樣<br>
```
def cmd(**kwargs):
    for key in kwargs:
        print(kwargs[key])
```
此時可以這樣呼叫：<br>
`cmd(firstName="Chang",lastName="Toby",nickName="Tobydog")`<br>
輸出結果為：<br>
```
Chang
Toby
Tobydog
```
如果有仔細看上方定義的函式就可以發現，兩個\*其實就是一個**dict**<br>
所以可以按照你的需求作使用<br>

##### 集大成
```
def cmd(arg,*args,**kwargs):
    return
```
此時在宣告時需要注意一點：\*參數的位置<br>
沒有\*的參數要放最前面，而兩個\*的要放在一個\*的前面<br>
且\*arg出現時不得有`def cmd(*,a,b)`這種關鍵字引數出現，但這兩者都可以搭配\*\*引數<br>
以上。



[^1]: 比較兩者是否皆為True

	  | AND | T | F |
	  |---|----|----|
	  |**T**|T|F|
	  |**F**|F|F|
[^2]: 比較兩者是否有一者為True

	  | OR | T | F |
	  |---|----|----|
	  |**T**|T|T|
	  |**F**|T|F|
[^3]:  轉換True, False

[^4]: AND 位數比對，比較兩者是否皆為1，並轉回十進位

	   數值| 十進位 | 二進位 |比較 |十進位
	   :----- | ----------:| ----------:| ----------:| ----------:
	   5 | 5|101|001|1
	   3 | 3|11|01|1

	   數值| 十進位 | 二進位 |比較 |十進位
	   :----- | ----------:| ----------:| ----------:| ----------:
	   13 | 13|1101|0101|5
	   5 | 5|101|101|5
[^5]: OR 位數比對，比較兩者是否有一項為1，並轉回十進位

	   數值| 十進位 | 二進位 |比較 |十進位
	   :----- | ----------:| ----------:| ----------:| ----------:
	   5 | 5|101|111|7
	   3 | 3|011|111|7

	   數值| 十進位 | 二進位 |比較 |十進位
	   :----- | ----------:| ----------:| ----------:| ----------:
	   13 | 13|1101|1101|13
	   5 | 5|0101|1101|13
[^6]: XOR 位數比對，比較兩者是否相反，並轉回十進位

	   數值| 十進位 | 二進位 |比較 |十進位
	   :----- | ----------:| ----------:| ----------:| ----------:
	   5 | 5|101|110|6
	   3 | 3|011|110|6

	   數值| 十進位 | 二進位 |比較 |十進位
	   :----- | ----------:| ----------:| ----------:| ----------:
	   13 | 13|1101|1000|8
	   5 | 5|0101|1000|8
