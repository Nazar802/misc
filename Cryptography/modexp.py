num=2813
mod=3223
i=0

for i in range(11):
    num=pow(num,2,mod)
    i+=1
    print(2**i, num)