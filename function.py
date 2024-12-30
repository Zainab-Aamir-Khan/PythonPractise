#calculate the average of three numbers

def newFunc(a,b,c):
    avg = (a+b+c)/3
    print(avg)

newFunc(3,5,6)
newFunc(3,4,8)

#to pass multiple values in a single line, we will use end=" "
#this is a built-in function
print("zainab",end=" ")
print("aamir")

print("maida")
print("aamir")
#these two will be printing on next lines

#len is also a builtin function
print(len("zainab"))

#we can also assign values in parameters,in this case arguments are not necessary
#default arguments
def def_para(a=2, b=4):
    prod = a * b
    print(prod)

def_para() #8

# WAF to print the length of a string
def _print():
    myPrint = "hello world"
    print(len(myPrint))

_print()
_print()
_print()
_print()



