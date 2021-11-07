import numpy
import matplotlib.pyplot as plt
from collections import Counter

def Matrix():
    
    #Ф(x)=x^31+x^27+x^23+x^19+x^15+x^11+x^10+x^9+x^7+x^6+x^5+x^3+x^2+x^1+1
    
    pol={0,1,2,3,5,6,7,9,10,11,15,19,23,27,31}
    
    global T
    global Q

    T0=numpy.array([0]*31,int)

    T1=numpy.identity(31,int)

    T2=numpy.vstack((T0, T1))

    T3=numpy.array([[0]*32]).T

    for j in pol:
        T3[j][0]=1
    
    T=numpy.column_stack((T2,T3))
    
    Q=T3
    
    return T

def M_Seq():
    
    f=open('LFSR.txt', 'a')
    
    global Q

    Q=numpy.dot(T,Q)%2
    
    sequence=Q.transpose()
    
    global integer
    integer=0
    for i in range(32):
        converted=(sequence[0][i])*(2**i)
        integer+=converted
    
    f.write(str(integer))
    
    return integer


if(__name__=="__main__"):
    
    Matrix()

    x=[]
    y=[]
    x.append(2147745793)

    for n in range(10000):
        M_Seq()
        x.append(integer)
        y.append(integer)

    y.append(2147745793)


    freq=Counter(x)
    seq=freq.keys()
    rep=freq.values()

    plt.bar(seq, rep, width=1e5)
    plt.xlabel('Числа')
    plt.ylabel('Кількість повторень')
    plt.show()

    plt.scatter(x, y, marker="s", s=1)
    plt.xlabel('X(i)')
    plt.ylabel('X(i+1)')
    plt.show() 