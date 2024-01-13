def fact(arg):
    if (arg==1 or arg ==0):
        return 1
    else:
        return arg*fact(arg-1)
x=fact(5)
print(x)