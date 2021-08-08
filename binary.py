binary = [1, 0, 0, 1, 1, 0, 1, 1] 
i=0
s=0
sum=0
length=len(binary)-1
while i<length:
    a=binary[i]
    s=(2**i)*a
    i+=1
    sum=+a
print(s)