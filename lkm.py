from collections import Counter
import matplotlib.pyplot as plt

f=open('lkm.txt', 'w')

a=1761  
b=7668  
x0=1576  
m=15125  

list=[]
list1=[]

xn=(a*x0+b)%m
list.append(xn)
f.write(str(xn))
x1=xn

for i in range(m-1):
    xn=(a*xn+b)%m
    list.append(xn)
    list1.append(xn)
    f.write(str(xn))

list1.append(x1)

freq=Counter(list)
seq=freq.keys()
rep=freq.values()
print(freq)

plt.bar(seq, rep, width=1)
plt.xlabel('Числа')
plt.ylabel('Кількість повторень')
plt.show()

x=list
y=list1
plt.scatter(x, y, marker="s", s=1)
plt.xlabel('X(i)')
plt.ylabel('X(i+1)')
plt.show()  