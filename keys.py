import math
from random import randint


def fermat():

    global p
    global q
    
    q=randint(2**1023, 2**1024-1)
    p=randint(2**1023, 2**1024-1)
    
    if(q%2==0):
        q+=1
    if(p%2==0):
        p+=1
  
    isPrime=False
    
    while(isPrime==False):
        
        if(pow(5,q-1,q)==1):
            isPrime==True
            break
            
        else:
            q+=2
    
    while(isPrime==False):
        
        if(pow(5,p-1,p)==1):
            isPrime==True
            break
            
        else:
            p+=2
    
    return 0


def modulo():

    global m
    global n
    global euler
    global q
    global p

    n=p*q
    euler=(p-1)*(q-1)
    m=n

    return n
    
def public(euler):
    
    for i in range(1, euler):
        e=randint(1, euler-1)
        if (math.gcd(e, euler)==1):
            break
    
    return e

def euclid(a, m):
    m0=m
    y=0
    x=1
 
    if(m==1):
        return 0
 
    while(a>1):
 
        q=a//m
        t=m

        m=a%m
        a=t
        t=y
 
        y=x-q*y
        x=t
 
    if(x<0):
        x=x+m0
 
    return x


def check():
    
    f=open('public_key.txt', 'w')
    s=open('secret_key.txt', 'w')
    mod=open('modul.txt', 'w')
    
    e=public(euler)
    d=euclid(e, euler)

    message=randint(2, n-1)

    cipher=pow(message, e, n)

    decipher=pow(cipher, d, n)
    
    if(decipher==message):
        f.write(str(e))
        s.write(str(d))
        mod.write(str(n))
        f.close()
        s.close
        mod.close


if (__name__=="__main__"):
    fermat()
    modulo()
    check()