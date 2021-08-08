li=[]
i=10
while i>0:
    num=int(input("enter a number"))
    li.append(num)
    i=i-1
print(num)
mam=int(input("enter a number"))
if mam in li:
    print("yes")
else:
    print("no")
    