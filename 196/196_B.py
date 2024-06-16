
import math
X = input()

if '.' in X:
    print(X[:X.index('.')])
else:
    print(X)