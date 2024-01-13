def anag(a,b):
    if len(a)!= len(b):
        print("\nnot anagrams")
    else:
        if sorted(a)==sorted(b):
            print("\nanagrams")
        else:
            print("\nnot anagrams")

a="abcdfe"
b="acbdef"
c=anag(a,b)
