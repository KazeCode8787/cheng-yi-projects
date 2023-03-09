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

song = "I have a pen. I have an apple, Apple pen. I have a pen. I have pineapple. Pineapple pen. Apple pen, pineapple pen, Pen Pineapple apple pen."
counts(replaceSymbols(song.lower()))
print(result)