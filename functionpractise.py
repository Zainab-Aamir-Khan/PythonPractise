#write a function to return a number whether it is even or odd by taking that number from the user

def evenOdd():
    number = int(input("enter any number: "))
    print(number)
    if number % 2 == 0:
        print("Even")
    else: 
        print("odd")

evenOdd()