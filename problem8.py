# Write a recursive function to calculate the sum of first n natural numbers.
def sum(n):
    if n==0:
        return 0
    return sum(n-1) + n

print(sum(10))



# Write a recursive function to print all elements in a list.
def myList(list, idx=0):
    if idx== len(list):
        return
    print(list[idx])
    myList(list, idx+1)

cities = ["Karachi", "Islamabad", "Lahore", "Murree"]
myList(cities)
