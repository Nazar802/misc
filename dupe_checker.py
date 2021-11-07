import hashlib as hs
import os
import sys
import time


start = time.time()
def hasher(file):
    BLOCK_SIZE = 65536
    hashed = hs.sha256()

    with open(file, 'rb') as f:
        fb=f.read(BLOCK_SIZE)

        while len(fb)>0: 
            hashed.update(fb) 
            fb=f.read(BLOCK_SIZE)
        
    dig=hashed.hexdigest()
    
    return dig

def lister():
    hashList = {}
    directory = sys.argv[1]
    for subdir, dirs, files in os.walk(directory):
        for file in files:
            fileName = os.path.join(subdir, file)
            hashList[fileName] = hasher(fileName)
    
    flipList = {}
    for key, value in hashList.items():
        flipList.setdefault(value, list()).append(key)
    
    return flipList

def checker():
    duplicates = [val[1:] for val in lister().values() if  len(val) > 1]
    return duplicates
    

if __name__ == "__main__":
    extra = checker()
    stop = time.time()
    duration = stop - start
    length = 0
    
    print("Directory {0} scanned in {1} seconds".format(sys.argv[1], duration))
    for group in extra:
        length += len(group)
        
    if len(extra) > 0:
        print("{0} duplicate files detected:\n{1}\nDo you want to remove them? (y/n)\n".format(length, extra))
        rem = input()
        if rem == "y":
            for dupe in extra:
                for dupeFile in dupe:
                    os.remove(dupeFile)
            print("Duplicate files successfully removed.")
    else:
        sys.exit(1)