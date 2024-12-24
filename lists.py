#lists
myList = ["zainab", "sana", "maida", "safaa", "zuneira"]
print(myList)
print(myList[0])
print(myList[4])

anyDataType = ["sana", 12, True, None]
print(anyDataType)


#List Slicing
print(anyDataType[0:3])
print(anyDataType[2:4])


#string methods
myAppend = anyDataType.append("zainab") #append will add a new list item
print(anyDataType)
print(myAppend)
print(anyDataType.clear()) #clear will remove all the list item

#sort method
mySort = ["sana", "safa", "zonu"]
newSort = mySort.sort()
print(mySort)

#reverse method
myReverse = ["zainab", "sana", "maida", "safaa" , "zuneira"]
newReverse = myReverse.reverse()
print(myReverse)

#insert method
myInsert = [12, 34 , 45]
newInsert = myInsert.insert(3, 32)
print(myInsert)

#pop method
myPop = [23,45,67,8,7]
newPop = myPop.pop(2)
print(myPop)

#remove method
myRemove = ["sana", "safa", "maida", "zainab", "zuneira"]
newRemove = myRemove.remove("zainab")
print(myRemove)



