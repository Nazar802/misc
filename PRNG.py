import math
from collections import Counter
from random import randint
import matplotlib.pyplot as plt
d=open('prng.txt', 'w')
f=open('print.txt', 'w')

pnum=randint(0, 1e4)

n=10011
list=[]
list.append(pnum)
list1=[]

for i in range(10010):
    pseudo=randint(1, 1e4)
    if (pseudo not in list):
        list.append(pseudo)
        list=list[-n:]
        list1.append(pseudo)
        list1=list1[-n:]
        binary=bin(pseudo)[2:].zfill((int)(math.log2(pseudo)))
        d.write(str(binary))
        f.write(str(pseudo))
    else:
        continue

d.close()
f.close()

print(len(list))

freq=Counter(list)
seq=freq.keys()
rep=freq.values()
print(freq)

list1.append(pnum)
plt.bar(seq, rep, width=1000)
plt.xlabel('Числа')
plt.ylabel('Кількість повторень')
plt.show()

x=list
y=list1
plt.scatter(x, y, marker="s", s=1)
plt.xlabel('X(i)')
plt.ylabel('X(i+1)')
plt.show()