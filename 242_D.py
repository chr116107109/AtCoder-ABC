
S = input()
Q = int(input())
N = len(S)
ABC = 'ABC'

def solve(S,N,K,T):
    diff = 0
    K -= 1
    while T > 0 and K > 0:
        if K%2 == 0:
            diff += 1
        else:
            diff += 2
        K //= 2
        T -= 1
    
    diff += T
    #print(K,diff)    
    return ABC[(ord(S[K])-65 + diff)%3]


for _ in range(Q):
    t,k = map(int,input().split())
    
    print(solve(S,N,k,t))