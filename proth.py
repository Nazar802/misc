from random import randint
import timeit

def prime_test():

    check=2**512
    
    if(check%2==0):
        check+=1
    
    
    while(pow(5,check-1,check)!=1):
        
        check+=2

    return check

def prime_test1():

    check=2**512
    
    if(check%2==0):
        check+=1
    
    
    while(pow(5,(check-1)>>1,check)!=-1):
        
        check+=2

    return check


print(timeit.timeit(lambda:prime_test(),number=1))
print(timeit.timeit(lambda:prime_test1(),number=1))