def rev(arg):
    y=""
    for i in arg:
        y=i+y
    return list(y)
a=["a",'h','o',"n",'d']
l=rev(a)
print(l)


