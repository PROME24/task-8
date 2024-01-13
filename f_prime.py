def num(x):
        count=0
        i=1
        for i in range(1,x+1):
            if(x%i==0):
                count=count+1
        if count==2:
            return x
        
        
        
s = [7,9,2,3,4,0,3,5]
for i in range(0,len(s)):
    print(num(s[i]))
