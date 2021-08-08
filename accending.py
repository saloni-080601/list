a=[43,12,44,33,2,11,8]
i=0
while i<len(a):
    j=0
    while j<len(a):
        if a[i]<a[j]:
            c=a[i]
            a[i]=a[j]
            a[j]=c
        j+=1
    i+=1
print(a)