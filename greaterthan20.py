num=[50, 40, 23,39, 70, 56, 12, 5, 10, 7] 
length=len(num)
index=0
i=0
j=0
while length>index:
    weadth=num[index]
    if weadth>20 and weadth<40:
        i+=1
    else:
        j+=1
    index=index+1
print("it is between 20 to 40:",i)
print("it is not between 20 to 40:",j)