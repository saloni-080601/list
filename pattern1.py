i=1
j=1
while i>=1:
    a=''*j+"*"*i+" "*j
    print(a,end=" ")
    i=i+1
    j=j+2
    print()
    if i>5:
       # break
        i=4
        j=1
        while i>=1:
            a=" "*j+"*"*i+" "*j
            print(a,end=" ")
            i=i-1
            j=j+1
            print()






