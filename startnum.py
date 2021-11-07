prime=[]
j=0

def prime_generator(x):
    for i in range(1, x):
        c=0
        for j in range (1, int(i/2)+1):
            if (i%j==0):
                c+=1
            if (j==prime):
                break
            if (c>1):
                break
        if (c==1):
            prime.append(i)
        
    return prime


