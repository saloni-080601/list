string="mehzabeen is a good girl"
list1=list(string)
i=0
a=" "
b=[]
count=0
while i<len(list1):
    if list1[i] not in a:
        b.append(list1)
        count+=1
    i+=1
print(count)
