class Lagrange:
    def __init__(self, pointlist):
        self.arPoints = pointlist

    def polinom(self):
        result = ''
        
        for i in range(len(self.arPoints)):
            p = str(self.arPoints[i][1]) + ' * '
            
            for j in range(i):
                p += '(x-' + str(self.arPoints[j][0]) + ')'
            for j in range(i+1, len(self.arPoints)):
                p += '(x-' + str(self.arPoints[j][0]) + ')'

            p += ' / '

            for j in range(i):
                p += '(' + str(self.arPoints[i][0]) + '-' + str(self.arPoints[j][0]) + ')'
            for j in range(i+1, len(self.arPoints)):
                p += '(' + str(self.arPoints[i][0]) + '-' + str(self.arPoints[j][0]) + ')'

            result += p + ' + '

        return result

    def getValue(self, x):
        result = 0
        for i in range(len(self.arPoints)):
            p = 1
            for j in range(i):
                p *= (x - self.arPoints[j][0]) / (self.arPoints[i][0] - self.arPoints[j][0])
            for j in range(i+1, len(self.arPoints)):
                p *= (x - self.arPoints[j][0]) / (self.arPoints[i][0] - self.arPoints[j][0])
            result += p * self.arPoints[i][1]   
        
        return result
class Chebyshev:
    def __init__(self, rank):
        self.rank = rank + 1
        self.koefs = self.__findkoefs()

    def koeficients(self):
        return self.koefs

    def roots(self):
        return np.roots(self.koefs)

    def Value(self, x):
        result = 0
        for i in len(self.koefs):
            result += x**(self.rank-i) * self.koefs[i]
        return result

    def __findkoefs(self):
        Tprev = [0] * self.rank
        Tprev[-1] = 1
        Tcurr = [0] * self.rank
        Tcurr[-2]  = 1
        for _ in range(2, self.rank):
            Ti = self.__Tnext(Tcurr, Tprev)
            Tprev = Tcurr
            Tcurr = Ti
        return Tcurr

    def __Tnext(self, Tcurr, Tprev):
        result = []
        buff = self.__slide(Tcurr)
        for i in range(self.rank):
            result.append(2 * buff[i] - Tprev[i])
        return result

    def __slide(self, array):
        result = []
        for i in range(len(array) - 1):
            result.append(array[i + 1])
        result.append(0)
        return result
import numpy as np
import math
import matplotlib.pyplot as plt
import random

def randNums(Xarray, lowerlim, upperlim):
    result = []
    for _ in Xarray:
        result.append(random.uniform(lowerlim, upperlim))
    return result

def optValuesX(start, end, count):
    polinom = Chebyshev(count)
    result = polinom.roots()
    for i in range(len(result)):
        result[i] = result[i] * (end-start)/2 + (start+end)/2
    return result

def equidistantValuesX(start, end, count):
    result = []
    step = (float)(end - start) / count
    for i in np.arange(start, end, step):
        result.append(i)
    return result

start = -1
end = 2
count = 8

X = optValuesX(start, end, count)
Y = randNums(X, -2, 4)
   
points = []
for i in range(count):
    points.append([X[i], Y[i]])

print(points)

polinom = Lagrange(points)

Xgraph = []
Ygraph = []
for i in np.arange(start, end, 0.005):
    Xgraph.append(i)
for x in Xgraph:
    Ygraph.append(polinom.getValue(x))

plt.plot(Xgraph, Ygraph)
plt.grid(True)
plt.show()

