import timeit
import math
from random import randint

def RSA():
    #print("Enter lower limit:")
    #lower=int(input())
    #print("Enter upper limit:")
    #upper=int(input())
    lower=10000
    upper=20000
    
    n=int(math.sqrt(upper-lower))
    prime=[]
    prime
    for i in range(lower, upper):
        c=0
        for j in range (1, int(i/2)):
            if (i%j==0):
                c+=1
        if (j==prime):
            continue
        elif (c==1):
            isprime=True
            prime.append(i)
            prime=prime[-n:]
            prime1.append(i)
            prime1=prime1[-n:]

    #print(prime)
    p=prime[randint(0, len(prime))]
    q=prime[randint(1, len(prime))]
    #print(p)
    #print(q)

    n=p*q
    euler=(p-1)*(q-1)

    print("modulus:", n)
    #print(euler)

    #public key
    for i in range(1, euler):
        e=randint(1, euler-1)
        if (math.gcd(e, euler)==1):
            print("public:", e)
            break
        
    #secret key
    for i in range(1, euler):
        if ((e*i)%euler==1):
            d=i
            print("secret:", d)
            break

    #encryption
    #print("Enter your message(int):")
    message=12345

    crypted=pow(message, e, n)
    print("crypted message:", crypted)

    #decryption
    decrypted=pow(crypted, d, n)
    print("decrypted message:", decrypted)
    
timeit.repeat("for x in range(1): RSA()", "from __main__ import RSA")
