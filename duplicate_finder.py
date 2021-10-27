import hashlib as hs
import zlib
import os
import sys
import time
import mysql.connector as mysql


def connect():
    return mysql.connect(host = "localhost", user = "DupeCheck", database = "Duplicates")

def crc(file):
    return "%X"%(zlib.crc32(open(file, 'rb').read()) & 0xFFFFFFFF)

def hasher(file):
    BLOCK_SIZE = 65536
    hashed = hs.sha256()

    with open(file, 'rb') as f:
        fb=f.read(BLOCK_SIZE)

        while len(fb)>0: 
            hashed.update(fb) 
            fb=f.read(BLOCK_SIZE)
    
    return hashed.hexdigest()

def lister(): 
    db = connect()
    add = db.cursor()
    crcList = []
    dirList = {}
    fileList = {}
    for subdir, dirs, files in os.walk(sys.argv[1]):
        for file in files:
            fileFullName = os.path.join(subdir, file)
            filePath = os.path.dirname(fileFullName)
            fileName = os.path.basename(file)
            fileCRC = crc(fileFullName)
            
            fileList[fileCRC] = fileFullName
                
            if fileCRC in crcList and dirList.get(fileCRC) == filePath:
                if hasher(fileList[fileCRC]) == hasher(fileFullName):
                    add.execute("INSERT INTO DuplicateFiles (File, Similar_To, Path, Filename, File_Hash) VALUES (%s, %s, %s, %s, %s)", (fileFullName, fileList[fileCRC], filePath, fileName, fileCRC))
            
            crcList.append(fileCRC)
            dirList[fileCRC] = filePath
            
    db.commit()
    
if __name__ == "__main__":
    start = time.time()
    lister()
    
    db = connect()
    querry = db.cursor()
    querry.execute("SELECT COUNT(*) FROM DuplicateFiles")
    length = querry.fetchone()[0]
    
    stop = time.time()
    duration = stop - start
    
    if length != 0:
        querry.execute("SELECT * FROM DuplicateFiles")
        dupeList = querry.fetchall()
        for item in dupeList:
            print(item, "\n")
        print("Directory {0} scanned in {1} seconds".format(sys.argv[1], duration))
        print("{0} duplicate files detected:".format(length))
        print("Do you want to remove them? (Y/N)")    
        decision = input()
        
        if decision == "y" or decision == "Y":
            querry.execute("SELECT File FROM DuplicateFiles")
            dupeList = querry.fetchall()
            fileToRemove = list(sum(dupeList, ()))
            for i in range(length):
                os.remove(fileToRemove[i])
            querry.execute("DELETE FROM DuplicateFiles")
            querry.execute("ALTER TABLE DuplicateFiles AUTO_INCREMENT = 1")
            db.commit()
            sys.exit(1)
        else:
            querry.execute("DELETE FROM DuplicateFiles")
            querry.execute("ALTER TABLE DuplicateFiles AUTO_INCREMENT = 1")
            db.commit()
            sys.exit(1)
    else:
        sys.exit(1)