import matplotlib.pyplot as plt
import pandas as pd

def calcSumToInf(exp):
    FX = eval(exp)
    fx = lambda x: FX
    x,y = [],[]
    tot = 0

    for i in range(1,100):
        for j in range(1,i):
            tot = fx(j)
        x.append(i)
        y.append(tot)
    
    drawGraph(x,y,exp)

def calcPoints(exp):
    x, y = [], []
    FX = eval(exp)
    fx = lambda x: FX

    for i in range (-100,100,1):
        x.append(i)
        y.append(fx(i))
    
    print(x,y)
    drawGraph(x,y,exp)

def drawGraph(x,y,exp):
    df = pd.DataFrame({
        'x_axis': x,
        'y_axis': y
    })
    
    #graph settings
    plt.ylim(-100, 100)
    plt.xlim(min(x), max(x))
    plt.title("y = "+exp)
    plt.ylabel(exp)
    plt.xlabel("x")
    plt.plot('x_axis', 'y_axis', data=df, linestyle='-', marker='.')
    plt.axvline(0, c='black', ls='--')
    plt.axhline(0, c='black', ls='--')
    
    plt.show()

