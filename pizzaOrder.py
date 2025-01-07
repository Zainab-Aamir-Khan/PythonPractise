print("welcome to Python pizza delieveries!!!")
size = input("what is the size of your pizza? L, M, or S?: ")
pepperoni = input("do you want extra pepperoni? Y or N: ")
cheese = input("do you want extra cheese for your on top of your pizza? Y or N: ")
bill = 0

# small pizza for 10 USD
# medium pizza for 15 USD
# large pizza for 20 USD
# pepperoni for small pizza +2 USD
# pepperoni for Large and Medium pizza +3 USD 
# extra cheese for any size of pizza +1 USD

if size == "S":
    bill = 10
elif size == "M":
    bill = 15
elif size == "L":
    bill = 20
else:
    print("you entered the wrong pricing!!")

if pepperoni == "Y":
    if size == "S":
        bill +=2
else: 
    bill +=3

if cheese == "Y":
    bill +=1

print(f"your final bill is ${bill}.")