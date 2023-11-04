import math

X = int(input())

keta = len(str(X))

if X >= 0:
    if X >= 10:
        ans = int(str(X)[:keta-1]) 
    else:
        ans = 0
else:
    if X <= -10:
        if str(X)[keta-1] == '0':
            ans = int(str(X)[:keta-1]) 
        else:
            ans = (int(str(X)[:keta-1]) - 1)
    else:
        ans = -1

print(ans)