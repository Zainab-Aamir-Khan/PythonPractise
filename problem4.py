#Write a program to store seven fruits in a tuple entered by the user
fruitOne = input("enter fruit name: ")
fruitTwo = input("enter fruit name: ")
fruitThree = input("enter fruit name: ")
fruitFour = input("enter fruit name: ")
fruitFive = input("enter fruit name: ")
fruitSix = input("enter fruit name: ")
fruitSeven = input("enter fruit name: ")
myTuple = (fruitOne, fruitTwo, fruitThree, fruitFour, fruitFive, fruitSix, fruitSeven)
print(myTuple)
print(type(myTuple))

# Write a program to accept marks of 6 students and display them in a sorted manner.
markOne = int(input("enter your marks : "))
markTwo = int(input("enter your marks : "))
markThree = int(input("enter your marks : "))
markFour = int(input("enter your marks : "))
markFive = int(input("enter your marks : "))
markSix = int(input("enter your marks : "))
marks = [markOne, markTwo, markThree, markFour, markFive, markSix]
marks.sort()
print(marks)

#Write a program to sum a list with 4 numbers.
mySum = [2,4,5,7,6]
print(sum(mySum))

#Write a program to count the number of zeros in the following tuple:
newTuple = (1,2,3,0,5,0,7,0)
oneTuple = newTuple.count(0)
print(oneTuple)






