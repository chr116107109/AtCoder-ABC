
import numpy as np
import itertools

N = int(input())

X = np.zeros(N)
Y = np.zeros(N)

for i in range(N):
    [X[i],Y[i]] = list(map(int,input().split()))

ind = np.argsort(X)
X = X[ind]
Y = Y[ind]

for i,j in itertools.combinations(N,2):
    x1 = X[i]
    x2 = X[j]
    y1 = Y[i]
    y2 = Y[j]
