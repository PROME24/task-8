def num(*arg):
    
    y=list(filter(lambda arg:arg%2!=0,arg))
    return y

x=num(1,2,3,4,2,6,5,7)
print(x)
                