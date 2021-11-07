import timeit
from functools import lru_cache

@lru_cache(maxsize=1)
def Luca_Lehmer(n):
    luca=4
    global sequence
    sequence=[]
    sequence.append(luca)
    for i in range(n):
        luca=luca**2-2
        sequence.append(luca)
    print(sequence)
    return sequence
    
@lru_cache(maxsize=1)
def Test(p):
    M=2**p-1
    #global isPrime
    #isPrime=False
    for i in range(len(sequence)):
        if (int(sequence[i])>M):
            factor=int(sequence[i])%M
            break
    
    for i in range(p):
        factor=pow(factor, 2, M)-2
        if (factor==0):
            print("2^%d-1 is prime" %p)
            #isPrime=True
            break
        if(i==p-1 and factor!=0):
            print("2^%d-1 is not prime" %p)
            #isPrime=False
            
Luca_Lehmer(16)
#Test(9689)
'''
mersenne=[]
for p in range(1,10000,2):
    Test(p)
    if (isPrime==True):
        mersenne.append(p)   

print(mersenne)'''

print(timeit.timeit(lambda:Test(86243), number=1))