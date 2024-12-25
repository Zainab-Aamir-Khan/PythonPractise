def myFunc(a,b,c):
    sum = a+b+c
    print(sum)
    return sum

myFunc(12,3,5)
myFunc(2,2,2)
myFunc("zainab ", "sana ", "maida")
myFunc(True, False, True) #2
myFunc(12.5, 32 , 45.5)

def names(std1 , std2, std3):
    print("the tallest student is : ", std3)
    return std3

names("Sana", "safa", "zainab") #calling method #1
names(std1 = "Sana", std2 = "Amir", std3 = "Maida") #calling method #2


# WAF to print the length of a list. ( list is the parameter)
def myList(newList):
    print(newList)
    print(len(newList))

myList(["mango", "banana", "oranges"])
myList(["Pakistan", "America", "Australia", "Peru"])






