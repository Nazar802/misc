import math
from random import randint


def prime_test():
    
    global prime
    prime=[]

    check1=randint(2**5, 2**6-1)
    check2=randint(2**5, 2**6-1)
    
    if(check1%2==0):
        check1+=1
    if(check2%2==0):
        check2+=1
  
    while(len(prime)!=1):
        
        if(pow(5,check1-1,check1)==1):
            prime.append(check1)
            break
        
        else:
            check1+=2
    
    while(len(prime)!=2):
        
        if(pow(5,check2-1,check2)==1):
            prime.append(check2)
            break
        
        else:
            check2+=2
            
    return prime


def modulus(prime):

    global m
    global n
    global euler
    
    p=prime[0]
    q=prime[1]

    n=p*q
    euler=(p-1)*(q-1)
    m=n

    print("modulus:", m)
    return n
    
def public(euler):
    
    for i in range(1, euler):
        e=randint(1, euler-1)
        if (math.gcd(e, euler)==1):
            print("public:", e)
            break
    
    return e

def secret(a, m):
    m0=m
    y=0
    x=1
 
    if(m==1):
        return 0
 
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
    
    f=open('Public.txt', 'w')
    s=open('Secret.txt', 'w')
    mod=open('Modulo.txt', 'w')
    
    e=public(euler)
    d=secret(e, euler)
    print("secret:", d)


    #encryption
    message=randint(2**3, n-1)

    crypted=pow(message, e, n)
    #print("crypted message:", crypted)

    #decryption
    decrypted=pow(crypted, d, n)
    #print("decrypted message:", decrypted)
    
    if(decrypted==message):
        f.write(str(e))
        s.write(str(d))
        mod.write(str(n))
        f.close()
        s.close
        mod.close


if __name__=="__main__":
    prime_test()
    modulus(prime)
    key_check()
