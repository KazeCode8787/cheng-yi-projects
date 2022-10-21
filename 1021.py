import keyword as ky
s1 = "HappyNewYear"
s2 = "happynewyear"
s3 = "new"

print(len(s1))
print(s1 == s2)
print(max(s1))
print(s3 in s1)
print(s1[4:9])

x = "Hello, World"
print(x.upper())
print(str.upper(x))
print(x.lower())
print(x.swapcase())
print(x.replace("World", "Tim"))
print(str.capitalize("an egg"))
print(str.title("an egg"))
print(str.isalpha("52apple"))
print(str.isalpha("asjkdjsk"))
print(str.isdigit("12354546"))
print(str.isdigit("sadjkl1"))
print(str.isalnum("123.55"))
print(str.isalnum("asds56sd"))
print(str.isupper("Hashdj"))
print(str.isupper("HASDLJK"))
print(str.islower("Hksdjks"))
print(str.islower("skdjskdj"))
print(str.isidentifier("1jkkjd"))
print(str.isidentifier("jkkjd"))
print(str.isidentifier('class'))
print(str.isspace("  "))
print(ky.iskeyword("None"))
print(str.istitle("Jks Jkasjd"))
x = "WowWowWowWowWow"
print(x.count('Wow'))
print(x.startswith("Wow"))
print(x.startswith("Ha"))
print(x.endswith("Wow"))
print(x.endswith("ha"))
print(x.find("Wow"))
print(x.rfind("Wow"))