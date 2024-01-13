def pal(arg):
    y=""
    for i in arg:
        y = i + y
    if (y==arg):
        return "palindrom"
    else:
        return "not palindrom"   
a=pal("1234321")
print(a) 