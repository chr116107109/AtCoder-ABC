
A,B = map(int,input().split())
A,B = min(A,B), max(A,B)

left = 0
right = 1000
epsilon = 10**(-10)

import math
while - left + right > epsilon:

    m = (left+right)/2

    l = 0
    r = A
    #print(left,right)
    possible = True
    while r - l > epsilon:
        
        x = (r+l)/2

        if x > m:
            r = x
            continue

        if math.sqrt(m**2 - x**2) > B:
            l = x
            possible = False
            continue

        if math.sqrt(3*(m**2-x**2))/2 + x/2 < A:
            possible = True
            break
        else:
            possible = False
            r = x
        
    #print(x)
    if possible:
        left = m
    else:
        right = m

print(left)
