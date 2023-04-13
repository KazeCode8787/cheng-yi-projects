import os
path = "C://poem.txt"
with open(path,"w") as f:
    f.write("asd\nioj\nkjsadlksjalkdjsalkdjls\njsaldkjcljsa\n21343424\n8324093\nkajdju3j\nsajdl")


if os.path.isfile(path):
    f = open(path,"r")
    for line in f:
        print(line)
    f.close()
else:
    print("file is not exist")
print(os.path.getsize(path))

fileObject = open(path,'r')

line = fileObject.readline()
while line != '':
    print(line)
    line = fileObject.readline()

fileObject.close()


with open(path) as f:
    content = f.read()
    print(content)


print(os.path.getsize(path))