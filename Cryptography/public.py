from random import randint

def prime_test():
    
    f=open('p.txt', 'w')
    global p
    p=randint(2**2047, 2**2048-1)
    
    if(p%2==0):
        p+=1
    
    isPrime=False
    
    while(isPrime==False):
        
        if(pow(5,p-1,p)==1):
            isPrime=True
        
        else:
            p+=2
    
    print(p)
    
    f.write(str(p))
    f.close()
    
    return p


def root(p):
    
    d=open('g.txt', 'w')
    
    euler=p-1
    factor=euler//2
    
    root=False
    
    while(root==False):
        
        g=randint(2**2047, p)
        
        if(pow(g,euler,p)==1):
            root=True
    
    print(g)
    
    d.write(str(g))
    d.close()
    
    return g

if __name__ == "__main__":
    prime_test()
    root(p)