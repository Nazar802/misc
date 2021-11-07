import math
import timeit
from functools import lru_cache
import gc

@lru_cache(maxsize=1)
def E_Sieve_Interval(lower, upper):
    if (lower%2==0):
        lower=lower+1
    initial=[True]*upper
    prime=[]
    for i in range(3, int(math.ceil(math.sqrt(upper))), 2):  
        if (initial[i]==True):  
            j=i*i
            while j<upper:
                initial[j]=False
                j+=i
        
    del initial[:lower]
    gc.collect()
    
    for n in range(0, upper-lower, 2):
        if (initial[n]==True):
            prime.append(n+lower)
    
    del initial
    gc.collect
    print(prime)
    return prime


@lru_cache(maxsize=1)
def E_Sieve(N):
    initial=[True]*N
    prime=[]
    for i in range(3, int(math.ceil(math.sqrt(N))), 2):  
        if (initial[i]==True):  
            j=i*i   
            while j<N:
                initial[j]=False
                j+=i

    for n in range(3, N, 2):
        if (initial[n]==True):
            prime.append(n)
    
    return prime

#print(timeit.timeit(lambda:E_Sieve(10000000), number=1))
print(timeit.timeit(lambda:E_Sieve_Interval(5000,10000), number=1))