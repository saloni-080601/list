a=[23,14,56,12,19,9,15,25,31,42,43]
i=0
j=0
c=0
sum=0
sam=0
while i<len(a):
    if a[i]%2==0:
        sum=sum+a[i]
        j+=1
    else:
        sam=sam+a[i]
        c+=1
    i+=1
print("odd:",sum/j)
print("even:",sam/c)    