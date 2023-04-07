path = "C://users/user/desktop/sus.txt"

with open(path,"w") as f:
    f.write("I have a pen. I have an apple, Apple pen. I have a pen. I have pineapple. Pineapple pen. Apple pen, pineapple pen, Pen Pineapple apple pen.")


result = {}


def replaceSymbols(string:str)->str:
    for char in string:
        if char in "~!@#$%^&*()_+\"/{}[]<>?,.":
            string = string.replace(char," ")
    return string


def counts(string:str)->None:
    wordList = string.split()
    for word in wordList:
        if word in result:
            result[word] = result[word] + 1
        else:
            result[word] = 1

f = open(path,'r')
song = f.read()
f.close()

counts(replaceSymbols(song.lower()))
print(result)