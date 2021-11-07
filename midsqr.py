import math
from collections import Counter
import matplotlib.pyplot as plt
import time

d=open('Middle-square.txt', 'w')
f=open('midint.txt', 'w')

begin=38**2
mid1=int(begin/10)
mid2=(int)(pow(10, ((int)(math.log10(begin))-1))*(int)(begin/pow(10, (int)(math.log10(begin)))))
mid=mid1-mid2

n=3001
list=[]
list.append(mid)

binary=bin(mid)[2:].zfill((int)(math.log2(mid)))
d.write(str(binary))
f.write(str(mid))

for i in range(3000):
    if math.log10(mid)>=1:
        loop=mid**2
        mid1=int(loop/10)
        mid2=(int)(pow(10, ((int)(math.log10(loop))-1))*(int)(loop/pow(10, (int)(math.log10(loop)))))
        mid=mid1-mid2
    else:
        loop=loop*10
        mid1=int(loop/10)
        mid2=(int)(pow(10, ((int)(math.log10(loop))-1))*(int)(loop/pow(10, (int)(math.log10(loop)))))
        mid=mid1-mid2
    if math.log10(mid)<=1:
        continue
    else:
        list.append(mid)
        list=list[-n:]
        binary=bin(mid)[2:].zfill((int)(math.log2(mid)))
        print(binary, end='', sep='')
        d.write(str(binary))
        f.write(str(mid))
    
d.close()
f.close()

freq=Counter(list)
seq=freq.keys()
rep=freq.values()
print(freq)

plt.bar(seq, rep)
plt.show()

time.sleep(60)