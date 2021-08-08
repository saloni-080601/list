num=[50,40,90,23,9,33,59,56,10,70,12,5,10,7,12]
a=[]
length=len(num)
smallest=num[0]
i=0
j=0
while i<length:
    s=num[i]
    while j<length:
        if num[j]<smallest:
            smallest=num[j]
            
        j=j+1
    i+=1 
print(smallest)