import random


L1=[1,2,3,4,5,6]
L2=[]

for i in range(10000):
    sum1=0
    count=0

    while sum1<7:
        sum1=sum1+random.choice(L1)
        count=count+1
    L2.append(count)

avg=sum(L2)/len(L2)
print(avg)
