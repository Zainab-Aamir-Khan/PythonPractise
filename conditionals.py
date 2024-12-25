#conditionals in python
name = "zainab"
if name == "sana":
    print(True)
else:
    print(False)

name1 = "Sana"
if name1 == "Safa":
    print("your name is safa")
elif name1 == "Zuni":
    print("your name is zuni")
else:
    print("who are you?")

#chained conditionals
name2 = "Zainab"
age = 21
if name2 == "Zainab":
    if age == 21:
        print("she is an adult")
    else:
        print("she is a kid")
else: 
    print("unknown")


#ternary conditional operators
print("kid" if age < 18 else "adult")




