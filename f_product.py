#Product of Arbitrary Arguments:
def pro(*arg):
    a=1
    for i in arg:
        a=a*i
    return a
r=pro(3,3,2,1)
print(r)    
