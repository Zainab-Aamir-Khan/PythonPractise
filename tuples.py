#tuples in python
myTuple = ("sana", "zainab", "safa", "zuneira", "zuneira")
print(myTuple)
print(type(myTuple))
yourTuple = [12, "zainab", True, False] #with different datatypes
print(yourTuple)
ourTuple = ("sana",)
print(ourTuple)
print(type(ourTuple))

firstTuple = ("sana")
print(firstTuple)
print(type(firstTuple))

name = ["sana"]
print(type(name))
print(name)

#the main difference between tuple and list is that there is not a single index in tuple, if we place a single index in a tuple, it will be string not a tuple, while in a list, we can place both longer list or only one index as well.


#tuple methods
tup = ("sana", "safa", "safa")
print(tup[1])
print(tup.count("safa"))