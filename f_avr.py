#Average of Arbitrary Arguments
def num(*arg):
    result=sum(arg)/len(arg)
    return result
avr=num(23,4,12,5,3)
print(avr)