a=["saloni","shivani","annu","annu","shivani","mehzabeen","nikita"]
i=0
let=[]
while i<len(a):
    j=0
    count=0
    while j<len(a):
        if a[i]==a[j]:
            count+=1
        j+=1
    if a[i] in let:
        i+=1
        continue
    let.append(a[i])
    let.append(count)
    print(a[i],"=",count)
print(let)
   