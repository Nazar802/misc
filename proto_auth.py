import hashlib as hs



def auth():
    
    print("Enter login: ")
    login=input()
    
    print("Enter password: ")
    password=input()
    
    loghash=hs.sha256()
    loghash.update(login.encode('utf8'))
    
    logdigest=str(loghash.hexdigest())
    
    passhash=hs.sha256()
    passhash.update(password.encode('utf8'))
    
    passdigest=str(passhash.hexdigest())
    
    with open('login.txt') as log:
        l=log.readlines()
    
    if l==logdigest and p==passdigest:
        print("Access granted")
    
    else:
        print("Wrong password and/or login")
        
    return 0



if __name__ == "__main__":
    
    auth()
