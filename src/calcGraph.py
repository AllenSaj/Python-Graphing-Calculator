import matplotlib.pyplot as plt
import pandas as pd

def calcSumToInf(n):
    total = 0
    for i in range(n):
        t = FX(i+1)
        total += t
    return total

def graph(exp):
    x, y = [], []
    n = 100
    fx = lambda x: eval(exp)

    for i in range (-n,n,1):
        x.append(i)
        y.append(fx(i))

    df = pd.DataFrame({
        'x_axis': x,
        'y_axis': y
    })

    plt.ylim(min(y), max(y)*1.1)
    plt.xlim(-n, n)
    plt.title("y = "+exp)
    plt.ylabel(exp)
    plt.xlabel("x")
    plt.plot('x_axis', 'y_axis', data=df, linestyle='-', marker='.')
    plt.axvline(0, c='black', ls='--')
    plt.axhline(0, c='black', ls='--')
    
    plt.show()

