import hashlib as hs

def hash():
    
    file=".\certificate.pdf"
    BLOCK_SIZE=65536
    
    hashed=hs.sha256() 
    with open(file,'rb') as f: 
        
        fb=f.read(BLOCK_SIZE) 

        while len(fb)>0: 
            hashed.update(fb) 
            fb=f.read(BLOCK_SIZE) 

    dig=hashed.hexdigest()
    
    global digest
    digest=int(dig, 16)

    print(digest)
    return digest


def signature():
    
    sg=open('Signature.txt', 'w')
    
    with open('Secret.txt') as sc:
        s=sc.read()
    
    secret=int(s)
    
    with open('Modulo.txt') as md:
        m=md.read()
        
    modulo=int(m)
    
    sign=pow(digest,secret,modulo)
    
    sg.write(str(sign))
    
    print(sign)
    return sign
    

if __name__=="__main__":
    hash()
    signature()
    