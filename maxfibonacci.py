from collections import Counter
import matplotlib.pyplot as plt

x0=5111
xn=10000
m=16384
f=open('fib.txt', 'w')


f.write(str(xn))
f.write("; ")

x=[]
y=[]
x.append(x0)
x.append(xn)
y.append(xn)
  
for i in range(10000):
    xn=(int(x[len(x)-1])+int(x[len(x)-2]))%m
    x.append(xn)
    y.append(xn)
    f.write(str(xn))
    f.write(' ')
    
f.close()

y.append(x0)

print(x)

freq=Counter(x)
seq=freq.keys()
rep=freq.values()
print(freq)

plt.bar(seq, rep, width=1)
plt.xlabel('Числа')
plt.ylabel('Кількість повторень')
plt.show()

plt.scatter(x, y, marker="s", s=1)
plt.xlabel('X(i)')
plt.ylabel('X(i+1)')
plt.show()