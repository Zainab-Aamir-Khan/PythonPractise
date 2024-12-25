# Print the elements of the following list using a loop:

# [1, 4, 9, 16, 25, 36, 49, 64, 81,100]

myList = [1, 4, 9, 16, 25, 36, 49, 64, 81,100]
for thisList in myList:
    print(thisList)


# Search for a number x in this tuple using loop:

# [1, 4, 9, 16, 25, 36, 49, 64, 81,100]
myTuple = [1, 4,9, 16, 25, 36, 49, 64, 81,100]
for myTuples in myTuple:
    if 9 in myTuple:
        print("yes")
        break
    else: 
        print("no")

# multiplication of a number using for loop and while loop
num = int(input("enter any number: "))
num1 = 0
for num1 in range(1, 11):
    print(num1*num)
    num1 +=1    

number1 = int(input("enter any number: "))           
number2 = 0
while number2 <= 10:
    print(number1*number2)
    number2 += 1


#Write a program to greet all the person names stored in a list ‘l’ and which starts with S.
namesOfFriends = ["sana", "safa", "sara", "zonu", "dina"]
for myFriend in namesOfFriends:
    print("Hi", myFriend)





