def num(n):
    li=[]
    for i in range(1,n+1):
        if(i==1):
            continue
        if n%i==0:
            count=0
            for j in range(2,i):
                if(i%j==0):
                    count=1
                    break
            if count==0:
                li.append(i)
    
    return li
    


n=int(input("\nenter a number  "))
a=num(n)
print(a)