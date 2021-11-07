from random import randint
import math

def prime_test():

    check=randint(2**8192,2**8193-1)
    
    if(check%2==0):
        check+=1
    
    
    while(pow(5,check-1,check)!=1):
        
        check+=2

    return check


def modulus():

    global euler
    global n
    
    p=prime_test()
    q=prime_test()

    n=p*q
    euler=(p-1)*(q-1)
    m=n

    return n
 

def public(euler):
    
    e=0
    
    while(math.gcd(e, euler)!=1):
        e=randint(1, euler-1)
    
    return e

    

def secret(a, m):
    
    m0=m
    y=0
    x=1
 
 
    while(a>1):
 
        # q is quotient
        q=a//m
 
        t=m
 
        # m is remainder now, process
        # same as Euclid's algo
        m=a%m
        a=t
        t=y
 
        # Update x and y
        y=x-q*y
        x=t
 
    # Make x positive
    if(x<0):
        x=x+m0
 
    return x


def key_check():
    
    f=open('keys16k.txt', 'a')
    
    e=public(euler)
    d=secret(e, euler)

    #encryption
    message=randint(2**512, n-1)
    
    crypted=pow(message, e, n)

    #decryption
    decrypted=pow(crypted, d, n)
    
    if(decrypted==message):
        f.write("Public:"+str(e)+"\n")
        f.write("Secret:"+str(d)+"\n")
        f.write("Modulo:"+str(n)+"\n")
        f.write("\n\n")
        f.close()


if __name__ == "__main__":
    modulus()
    key_check()
