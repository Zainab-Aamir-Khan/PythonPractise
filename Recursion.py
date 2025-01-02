#recursive function
def recFunc(n):
    if(n==0):  #base case
        return
    print(n)
    recFunc(n-1)
    print("DEAD!!!")

recFunc(6)

#call stack --> calling a function repeatedly



#find the factorial of n number through recursion 
def fact(n):
   if n==1 or n==1:
       return 1
   else:
    return (n * fact(n-1))

print(fact(5))