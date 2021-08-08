number=30
list1=[10,11,12,13,14,17,18,19,20]
z=[]
i=0
while i<len(list1):
    j=0
    while list1[i]>list1[j]:
        if number==list1[i]+list1[j]:
            z.append([list1[j],list1[i]])
        j=j+1
    i+=1
print(z)

