from random import randint
import matplotlib.pyplot as plt

def plot():
    
    global xaxis
    global yaxis
    xaxis=[]
    yaxis=[]
    xaxis.append(32751)
    for i in range(10000):
        random=randint(0,32767)
        xaxis.append(random)
        yaxis.append(random)

    yaxis.append(32751)
    
    plt.scatter(xaxis, yaxis, marker="s", s=1)
    plt.xlabel('X(i)')
    plt.ylabel('X(i+1)')
    plt.show()
    
    return plt.show()
