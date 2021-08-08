user = [3000, 600000, 324990909, 90990900, 30000, 5600000, 690909090, 31010101, 532010, 510, 4100] 
i=0
diwale=0
lakhpati=0
crorepati=0
while i<len(user):
    if user[i]<100000:
        diwale=diwale+1
    elif user[i]>100000 and user[i]<10000000:
        lakhpati=lakhpati+1
    else:
        crorepati=crorepati+1
    i+=1
print("diwale",diwale)
print("lakhpati",lakhpati)
print("crorepati",crorepati)            