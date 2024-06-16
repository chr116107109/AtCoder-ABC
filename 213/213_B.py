import numpy as np

N = int(input())
A = list(map(int, input().split()))
A = np.array(A)

ind = np.argsort(A)

#print(ind)
print(ind[-2]+1)
