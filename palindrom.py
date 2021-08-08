name=input("enter a string")
length=len(name)
first=0
i=0
li=list(name)
while first<length-1:
    print(li)
    if name[first+i]==name[length-1]:
        print("yes")  
    else:
        print("no")
    break

        