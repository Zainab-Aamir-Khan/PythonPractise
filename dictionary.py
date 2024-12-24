#dictionary
myDic = {
    "name" : "zainab",
    "age" : 21,
    "degree" : "CS",  
    "IsAdult" :True,
    "mylist" : ["sana", "safaa", "zonu"]
}
print(myDic)

#to print the specific key's value of the dictionary
print(myDic["name"])
print(len(myDic))
print(type(myDic))
print(myDic.items())
print(myDic.keys())
print(myDic.values())
myDic.update({"name" : "safa"})
print(myDic)
print(myDic.get("age"))



