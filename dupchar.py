char = ["a", "n", "t", "a", "a", "t", "n", "n", "a", "x", "u", "g", "a", "x", "a"] 
i=0
lit=[]
while i<len(char):
    j=0
    count=0
    while j<len(char): 
        if char[i]==char[j]:
            count=count+1
        j+=1
    if char[i] in lit:
        i+=1
        continue
    lit.append([char[i],count])
print(lit)