# Write a program to create a dictionary of english words with values as their urdu translation.
myDict = {
    "great" : "acha",
    "life" : "zindagi",
    "grave" : "qabar"
}
print(myDict)

# Write a program to input eight numbers from the user and display all the unique numbers (once)
num1 = int(input("enter any number: "))
num2 = int(input("enter any number: "))
num3 = int(input("enter any number: "))
num4 = int(input("enter any number: "))
num5 = int(input("enter any number: "))
num6 = int(input("enter any number: "))
num7 = int(input("enter any number: "))
num8 = int(input("enter any number: "))
mySet = {num1, num2, num3,num4,num5,num6,num7,num8}
print(mySet)
#its output will be amazing, if you enter 2 similar numbers, it will not return that similar number but just once because sets do not repeat the similar numbers


#Can we have a set with 18 (int) and '18' (str) as a value in it? the answer is yepppppp!!!!!!!!
myNewSet = {18, "18"}
print(myNewSet)

emptySet = set() #we can do this with set constructor not just simple set
emptySet.add("A")
emptySet.add("B")
print(emptySet)
print(len(emptySet))


#s = {} What is the type of 's'?
s = {}
print(type(s))
print(s)


# problem #6 Create an empty dictionary. Allow 4 friends to enter their favorite language as value and use key as their names. Assume that the names are unique
emptyDict = {
    input("enter name : ") : input("enter language : "),
    input("enter name : ") : input("enter language : "),
    input("enter name : ") : input("enter language : "),
    input("enter name : ") : input("enter language : ")
}
print(emptyDict)


#If the names of 2 friends are same; what will happen to the program in problem 6?
print(emptyDict)
print("in this case it will only print one key-value only")


# If languages of two friends are same; what will happen to the program in problem 6?
print(emptyDict)
print("in this case it will print both key value, it shows that keys hold a special position in dictioanry w.r.t repitition but values do not")


#Can you change the values inside a list which is contained in set S? s = {8, 7, 12, "Harry", [1,2]}
s = {8, 7, 12, "zainab", [1,2]}
print("Sets items are unchangeable")



