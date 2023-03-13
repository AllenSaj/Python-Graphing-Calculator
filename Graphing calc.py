import math
import matplotlib.pyplot as plt
import pandas as pd


def calcSumToInf(n):
    total = 0
    for i in range(n):
        t = FX(i+1)
        total += t
    return total


c1 = input('''What would you like to do?
1. Sum to infinity
2. Graphing
''')

c2 = input('''What would you like to do?
1. y = x**-2
2. y = x**-0.5
3. Enter your equation
''')

global FX, TXT
x, y = [], []
n = 100
hasRun = False

if c2 == "1":
    FX = lambda x: 1/x**2
    TXT = "1/x**2"
elif c2 == "2":
    FX = lambda x: 1/x**0.5
    TXT = "1/x**-0.5"
elif c2 == "3":
    TXT = input("Please enter your equation (f(x) = ):")
    FX = lambda x: eval(TXT)

if c1 == "1":
    for i in range (n):
        x.append(i+1)
        y.append(calcSumToInf(i+1))
elif c1 == "2":
    for i in range (-n,n,1):
        if i == -1:
            continue
        x.append(i+1)
        y.append(FX(i+1))

df = pd.DataFrame({
      'x_axis': x,
      'y_axis': y
})

if c1 == "1":
    TXT = "Sum of "+TXT
    plt.ylim(0, (max(y)*1.1))
    plt.xlim(0, n)
else:
    plt.ylim(min(y), max(y)*1.1)
    plt.xlim(-n, n)
plt.title("y = "+TXT)
plt.ylabel(TXT)
plt.xlabel("x")
plt.plot('x_axis', 'y_axis', data=df, linestyle='-', marker='.')
plt.axvline(0, c='black', ls='--')
plt.axhline(0, c='black', ls='--')
  
plt.show()

