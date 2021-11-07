from collections import Counter
import matplotlib.pyplot as plt

a=87
b=234
x0=111
m=16384
f=open('fib.txt', 'w')

xn=(a*x0+b)%m
f.write(str(xn))
f.write("; ")

x=[]
y=[]
x.append(x0)
x.append(xn)
y.append(xn)

for i in range(8):
    xn=(a*xn+b)%m
    x.append(xn)
    y.append(xn)
    f.write(str(xn))
    f.write("; ")
    
for i in range(10000):
    xn=(int(x[len(x)-7])+int(x[len(x)-10]))%m
    x.append(xn)
    y.append(xn)
    f.write(str(xn))
    f.write(' ')
    
f.close()

y.append(x0)


freq=Counter(x)
seq=freq.keys()
rep=freq.values()
print(freq)

plt.bar(seq, rep, width=5)
plt.xlabel('Числа')
plt.ylabel('Кількість повторень')
plt.show()

plt.scatter(x, y, marker="s", s=1)
plt.xlabel('X(i)')
plt.ylabel('X(i+1)')
plt.show()