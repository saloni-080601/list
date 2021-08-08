num=[50,40,23,9,33,56,70,12,5,90,10,7,90,100]
i = 0
max_num = 0
while i<len(num):
    if max_num<num[i]:
       max_num = num[i]
    i = i+1
print(max_num)