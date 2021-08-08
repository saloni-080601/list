li=[]
i=5
rev=0
while i>0:
    num=input("enter a string")
    li.append(num)
    i=i-1
print(li)
# i=0
rev=len(li)
index=1
while index<=rev:
    print(li[-index],end=" ,") 
    index=index+1
