#Write a program to print yes when the age entered by the user is greater than or equal to 18
age = int(input("enter your age: "))
if age >= 18:
    print("Yes")


# Write a program to find the greatest of four numbers entered by the user.
num1 = int(input("enter any number: "))
num2 = int(input("enter any number: "))
num3 = int(input("enter any number: "))

numbers = num1, num2, num3
print(max(numbers))

# Write a program to find out whether a student has passed or failed if it requires a
# total of 40%. Assume 3 subjects and
# take marks as an input from the user.

urdu = int(input("enter your urdu marks: "))
english = int(input("enter your english marks: "))
maths = int(input("enter your maths marks: "))
total = urdu + english + maths
percentage = total/300*100
if percentage == 40:
    print("passed")
else: 
    print("failed")



# A spam comment is defined as a text containing following keywords:
# “Make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a program
# to detect these spams.
keyword = input("enter any msg: " )
if keyword == "buy now" or "subscribe this" or "click this":
    print("these msgs are spam")


# Write a program to find whether a given username contains less than 10
# characters or not.
username = "zainabaamir088"
if len(username) >= 10:
    print("it has", len(username), "characters")
else:
    print("it has less than 10 characters")


# Write a program which finds out whether a given name is present in a list or not.
num  = [3,2,4,5,78,9]
myNum = int(input("enter any number: "))
if myNum in num:
    print(myNum, "is present")
else:
    (myNum, "is not present")


# Write a program to find out whether a given post is talking about "zainab" or not.
post = "zainab"
if post == "zainab":
    print("the post is talking abt zainab")