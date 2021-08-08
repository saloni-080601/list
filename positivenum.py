a=[23,14,56,12,19,9,15,25,31,42,43]
i=0
j=0
c=0
sum=0
sam=0
u=0
som=0
while i<len(a):
    som=som+a[i]
    if a[i]%2==0:
        sum=sum+a[i]
        j+=1
    else:
        sam=sam+a[i]
        c+=1
    u+=1
    i+=1
print("count even",j)
print("count odd",c)
print("count whole",u)
print("sum even",sum)
print("sum odd",sam)
print("sum whole",som)
print("ave even:",sum/j)
print("ave odd:",sam/c)   
print("total number",som/u) 