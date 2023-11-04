
N = int(input())
import math
def combinations_count(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

def f(N):
    if N == 0:
        return 1
    m = 0
    while 3**m <= N:
        m += 1
    
    ans = 0
    #print(N,m)
    for i in range(m+1):
        ans += combinations_count(m,i)*f(N//(2**(m-i) * 3**i))
    
    return ans

print(f(N))
