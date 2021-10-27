import numpy as np
import statistics as st

L1=[]
for i in range(10000):
    sum1=0
    count=0

    while sum1<1:
        sum1=sum1+np.random.uniform(0,1,None)
        count=count+1
    L1.append(count)

#Aver= st.mean(L1)
#print(Aver)

avg=sum(L1)/len(L1)
print(avg)


