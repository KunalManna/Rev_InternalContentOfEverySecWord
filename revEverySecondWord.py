# Revese internal content of every second word a string

def revEverySecWord(s):
    p=s.split()
    n=len(p)
    i=0
    l=[]
    while(i<n):
        if i%2==0:
            l.append(p[i])
        else:
            l.append(p[i][::-1])
        i=i+1
    output=' '.join(l)
    return output
    



s=input("Enter the string:\n")               # one two three four five six
ans=revEverySecWord(s)
print(ans)                                   # one owt three ruof five xis
