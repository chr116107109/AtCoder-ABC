

N,x,y = map(int,input().split())
A = list(map(int,input().split()))

A_odd = [A[i] for i in range(N) if i%2==1]
A_even = [A[i] for i in range(N) if i%2==0]


def can_reach_even(A,value):
    M = 2*(10**4)+1
    d = [[0]*(M) for i in range(len(A)+1)]
    d[0][0] = 1
    d[1][A[0]] = 1
    for k in range(2,len(A)+1):
        
        for i in range(M):
            if d[k-1][i] == 1:
                d[k][(i+A[k-1])%M] = 1
                d[k][i-A[k-1]] = 1

    #print(d)
    if d[len(A)][value] == 1:
        return True
    else:
        return False

def can_reach_odd(A,value):
    M = 2*(10**4)+1
    d = [[0]*(M) for i in range(len(A)+1)]
    d[0][0] = 1
    for k in range(1,len(A)+1):
        
        for i in range(M):
            if d[k-1][i] == 1:
                d[k][(i+A[k-1])%M] = 1
                d[k][i-A[k-1]] = 1
    #print(d)
    if d[len(A)][value] == 1:
        return True
    else:
        return False

if can_reach_odd(A_odd,y) and can_reach_even(A_even,x):
    print('Yes')
else:
    print('No')