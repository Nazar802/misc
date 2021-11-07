def rwh_primes2(n):
    # http://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
    """ Input n>=6, Returns a list of primes, 2 <= p < n """
    correction = (n%6>1)
    n = {0:n,1:n-1,2:n+4,3:n+3,4:n+2,5:n+1}[n%6]
    sieve = [True] * (n//3)
    sieve[0] = False
    for i in range(int(n**0.5)//3+1):
      if sieve[i]:
        k=3*i+1|1
        sieve[      ((k*k)//3)      ::2*k]=[False]*((n//6-(k*k)//6-1)//k+1)
        sieve[(k*k+4*k-2*k*(i&1))//3::2*k]=[False]*((n//6-(k*k+4*k-2*k*(i&1))//6-1)//k+1)
    return [2,3] + [3*i+1|1 for i in range(1,n//3-correction) if sieve[i]]


LIMIT = 1000000
PRIME_LIST = rwh_primes2(LIMIT)



# A number is prime if and only if it is not divisible by any prime lower than its square root.
def is_Prime(num):
    for i in PRIME_LIST:
        if i*i> num:
            return True
        elif num%i == 0:
            return False
    return True



# Return a sorted list of possible primes lower than limit.
def possiblePrimes(limit):
    l = []
    # 2**i -1 (Mersenne primes)
    i = 2
    while(i < limit):
        l.append(i-1)
        i *= 2
    # n! + 1 or n! -1 (Factorial primes)
    i = 2
    n = 2
    while(i < limit):
        l.append(i-1)
        l.append(i+1)
        n += 1
        i *= n
    return sorted(list(l))



bigPrime = 0
candidates = possiblePrimes(LIMIT*LIMIT)
for c in candidates:
    if(is_Prime(c)):
        bigPrime = c



print(bigPrime)