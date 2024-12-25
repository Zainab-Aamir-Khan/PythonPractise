#loops in python

num = 0
while(num <= 5):
    print(num)
    num = num + 1

i = 1
while(i <= 5):
    print("zainab")
    i= i + 1 

# Write a program to print 1 to 50 using a while loop
num1 = 1
while(num1 <= 50):
    print(num1)
    num1 +=1


#for loop
#loop through a list, set, dictionary, or tuple
friends = ["zuneira", "hafsa", "amna", "lareb", "eeshah"] #list
for friend in friends:
    print(friend)

countries = {"Pakistan", "KSA", "UAE", "USA", "UK"}
for country in countries:
    print(country)

x = 0
for x in range(2, 11, 2):
    print(x)



# for loop with else:
number = [2,3,4,5,7]
for numbers in number:
    print(numbers)
else: 
    print("done") #to print something in the end



#break statement in for loop
a = 0
for a in range(2, 30):
    print(a)
    if a == 20:
        break


print("lets play with continue statement")
#continue in for loop
b = 0
for b in range(2,10):
    if b == 7:
        continue
    print(b)


#pass statement
myPass= 0
for myPass in range(23,43):
    pass

