marks=[[78,76,94,86,88],[91,71,98,65],[95,45,78],[87,67,49,68,88]]
i=0
sum=0
j=0
while i<len(marks):
    j=0
    while j<len(marks[i]):
        sum=sum+marks[i][j]
        j+=1
    i+=1
print(sum/2)