a=["saloni","nikita","mehzabeen","salonipanwar"]
i=0

while i<len(a):
    j=0
    count=0
    list1=list(a[i])
    while j<len(list1):
        count+=1        
        j+=1
    if count%2==0:
        print(a[i])    
    i+=1