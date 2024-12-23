#there are 3 ways to write a string
print("hello world")
print("""hello world""")
print('hello world')

#string slicing
name = "zainab is a python developer"
print(name)
print(name[:5])# this will print from start but end at 4th index which is "a"
print(name[2: ]) # this will start from 3rd index and will print all the remaining letters till the end
print(name[3 : 6]) # this will print the letters from 3rd index to 6th index 
print(name[-1]) # this will print the last letter


#slicing with a skip value
remarks = "wonderful"
print(remarks[2 : 8 : 2]) #nef
#here 2 is the start 8 is the end and 2 is the number of skips


#String functions
word = "zainabaamir"
print(len(word)) #this will return the length of the str
print(word.endswith("ir")) #this is return output in boolean 
print(word.endswith("na"))
print(word.count("a")) #will count the specific character occurence
capitalizedString = word.capitalize()
print(capitalizedString)#it will convert first character into UC 
indexString = word.index("i") #it will point out the index of i
print(indexString)
replaceString = word.replace("a","s" )#it will replace character a with s
print(replaceString)
findString = word.find("z")# it will find the character 
print(findString)


#escape sequence characters
print("ola, my name is \"zainab aamir\"\n and i am a\t developer, and my\\ work is to have a lot of coffee ")
