'''def fast_inverse(e, m):
    m0=m
    u=1
    v=0
    
    while (m>1):
        m=e%m
        q=m//e
        u=u-q*v
        v=v-q*u
        
    d=v
    print(d)
    
fast_inverse(10, 13) '''

def modInverse(a, m):
    m0 = m
    y = 0
    x = 1
 
    if (m == 1):
        return 0
 
    while (a > 1):
 
        # q is quotient
        q = a // m
 
        t = m
 
        # m is remainder now, process
        # same as Euclid's algo
        m = a % m
        a = t
        t = y
 
        # Update x and y
        y = x - q * y
        x = t
 
    # Make x positive
    if (x < 0):
        x = x + m0
 
    return x

print(modInverse(101, 275))

