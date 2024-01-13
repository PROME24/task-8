# Count Occurrences:
def Count(*arg):
    for i in arg:
        count=0
        for j in arg:
            if(i==j):
                count =count + 1
        print(f"{i} has occured {count} times\n")

num = Count(3,4,5,6,5,6,2,3,3,4)