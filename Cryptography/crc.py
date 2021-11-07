import zlib

def check(file):
    return "%X"%(zlib.crc32(open(file, 'rb').read()) & 0xFFFFFFFF)


file = "./dung1.txt"
print(check(file))        