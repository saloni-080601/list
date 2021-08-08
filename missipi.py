a=["missippi"]
i=0
b=list(a[i])
print(b)
c=[]
while i<len(b):
    if b[i] not in c:
        c.append(b[i])
    i+=1
print(c)
j=0
m=0
while j<len(c):
    k=0
    count=0
    while k<len(b):
        if c[j]==b[k]:
            count+=1   
        k+=1
    print(c[j],"=",count)
    j+=1