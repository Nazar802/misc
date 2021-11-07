from plot import plot
import numpy as np
import matplotlib.pyplot as plt
import pylfsr
from collections import Counter


'''
x^15 + x^1 + 1
x^15 + x^4 + 1
x^15 + x^7 + 1
x^15 + x^7 + x^6 + x^3 + x^2 + x^1 + 1
x^15 + x^10 + x^5 + x^1 + 1
x^15 + x^10 + x^5 + x^4 + 1
x^15 + x^10 + x^5 + x^4 + x^2 + x^1 + 1
x^15 + x^10 + x^9 + x^7 + x^5 + x^3 + 1
x^15 + x^10 + x^9 + x^8 + x^5 + x^3 + 1
x^15 + x^11 + x^7 + x^6 + x^2 + x^1 + 1
x^15 + x^12 + x^3 + x^1 + 1
x^15 + x^12 + x^5 + x^4 + x^3 + x^2 + 1
x^15 + x^12 + x^11 + x^8 + x^7 + x^6 + x^4 + x^2 + 1
x^15 + x^14 + x^13 + x^12 + x^11 + x^10 + x^9 + x^8 + x^7 + x^6 + x^5 + x^4 + x^3 + x^2 + 1
'''

fpoly=[[15,4],[15,1],[15,7],[15,7,6,3,2,1],[15,10,5,1],[15,12,11,8,7,6,4,2],[15,10,5,4,2,1],[15,10,9,7,5,3],[15,10,9,8,5,3],[15,11,7,6,2,1],[15,12,3,1],[15,12,5,4,3,2],[15,12,11,8,7,6,4,2],[15,14,13,12,11,10,9,8,7,6,5,4,3,2],[15,10,9,8,5,3]]

binpol=[]
bpoly=[]
for l in range(len(fpoly)):
    fpol=fpoly[l]
    for m in fpol:
        binpol=[1]*15
        binpol[0]=0
        binpol[m-1]=0
    bpoly.append(binpol)
        

L=pylfsr.LFSR(fpoly=fpoly[1],initstate=bpoly[0],verbose=False)
temp=L.runKCycle(15)

x=[]
y=[]

x.append(32751)

f=open('gollman.txt', 'w')

seq=0
for j in range(10000):
    
    for i in range(15):
        L.runKCycle(15)
        temp=L.state
        seq=temp&seq
        
        if (seq[0]==1):
            L=pylfsr.LFSR(fpoly=fpoly[i],initstate=seq,verbose=False)
            integer=0
            
            for k in range(len(temp)):
                dec=temp[k]*2**k
                integer+=dec
                f.write(str(integer))
                
            x.append(integer)
            y.append(integer)
            
        else:
            integer=0
            for k in range(len(temp)):
                dec=temp[k]*2**k
                integer+=dec
            f.write(str(integer))
            x.append(integer)
            y.append(integer)
            break

f.close()

y.append(32751)
freq=Counter(x)
seq=freq.keys()
rep=freq.values()

plt.bar(seq, rep,width=1)
plt.xlabel('Числа')
plt.ylabel('Кількість повторень')
plt.show()
plot()