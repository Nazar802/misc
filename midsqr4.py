import math
from collections import Counter
import matplotlib.pyplot as plt

d=open('midsqr.txt', 'w')
f=open('midsqrbin.txt', 'w')

n=20001
list=[]
list1=[]

begin=36326632**2
mid1=int(begin/10000)
mid2=(int)(pow(10, ((int)(math.log10(begin))-7))*(int)(begin/pow(10, (int)(math.log10(begin))-3)))
mid=mid1-mid2
midb=mid1-mid2
list.append(mid)
loop=mid**2

for i in range(15137):
    if math.log10(mid)>=7:
        loop=mid**2
        mid1=int(loop/10000)
        mid2=(int)(pow(10, ((int)(math.log10(loop))-7))*(int)(loop/pow(10, (int)(math.log10(loop))-3)))
        mid=mid1-mid2
        if mid==0:
            print(i)
            break
    else:
        loop=loop*10
        mid1=int(loop/10000)
        mid2=(int)(pow(10, ((int)(math.log10(loop))-7))*(int)(loop/pow(10, (int)(math.log10(loop))-3)))
        mid=mid1-mid2
    if math.log10(mid)<=7:
        continue
    else:
        list.append(mid)
        list=list[-n:]
        list1.append(mid)
        list1=list1[-n:]
        binary=bin(mid)[2:].zfill((int)(math.log2(mid)))
        d.write(str(mid))
        f.write(str(binary))
    
list1.append(midb)
    
freq=Counter(list)
seq=freq.keys()
rep=freq.values()
y=freq.keys()
print(freq)

plt.bar(seq, rep, width=5000)
plt.xlabel('Числа')
plt.ylabel('Кількість повторень')
plt.show()


x=list
y=list1
plt.scatter(x, y, marker="s", s=1)
plt.xlabel('X(i)')
plt.ylabel('X(i+1)')
plt.show()

input()