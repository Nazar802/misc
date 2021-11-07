import timeit
from random import randint
import math

def prime_test(N):
    
    global prime
    prime=[]

    check1=randint(2**(N-1), 2**N-1)
    #print("initial",check1)
    check2=randint(2**(N-1), 2**N-1)
    #print("initial",check2)
    
    if(check1%2==0):
        check1+=1
    if(check2%2==0):
        check2+=1

    
    while(len(prime)!=1):
        
        if(pow(5,check1-1,check1)==1):
            prime.append(check1)
            #print(check1)
            break
        
        else:
            check1+=2
            #print(check1)
    
    while(len(prime)!=2):
        
        if(pow(5,check2-1,check2)==1):
            prime.append(check2)
            #print(check2)
            break
        
        else:
            check2+=2
            #print(check2)
            
    print(prime)
    return prime
    

def prime_test2():
    
    global prime
    prime=[]

    while(len(prime)<=2):
        
        check=randint(2**2047, 2**2048-1)
        
        if(pow(5,check-1,check)==1):
            prime.append(check)

    print(prime)
    return prime

 
print(timeit.timeit(lambda:prime_test(2048),number=1))
print(timeit.timeit(lambda:prime_test2(),number=1))