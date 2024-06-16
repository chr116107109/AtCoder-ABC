

from re import A


def f(a,b):
    return (a+b)**3 - 2*a*b*(a+b)

N = int(input())

M = (10**6)

ans = 10**30
for i in range((M+1)):
    a = i
    left = i
    right = M

    while left < right:
        b = (left + right)//2
        if f(a,b) < N:
            left = b + 1
        else:
            right = b 

    #print(a,b,f(a,b))    
    ans = min(f(a,left),ans)

print(ans)
