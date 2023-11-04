
N,L,R = map(int,input().split())
A = list(map(int,input().split()))

import random
def main():
    #N,L,R = 100, random.randint(-1000,1000), random.randint(-1000,1000)
    #A = [random.randint(-1000,1000) for i in range(N)]

    def naive(A,N,L,R):
        val = 10**10
        for i in range(N+1):
            for j in range(i,N+1):
                val = min(L*i+sum(A[i:j])+(N-j)*R, val)
        return val

    #val = naive(A,N,L,R)
    import copy
    A_c = copy.deepcopy(A)

    dl = [0] * (N+1)
    dl[1] = min(L,A[0])
    l = 0
    for i in range(2,N+1):
        if dl[i-1] + A[i-1] > L*(i):
            dl[i] = L*(i)
        else:
            dl[i] = dl[i-1] + A[i-1]
        
    A.reverse()

    dr = [0] * (N+1)
    dr[1] = min(R,A[0])
    for i in range(2,N+1):
        if dr[i-1] + A[i-1] > R*(i):
            dr[i] = R*(i)
        else:
            dr[i] = dr[i-1] + A[i-1]


    min_val = 10**30
    for i in range(N+1):
        min_val = min(min_val, dl[i]+dr[N-i])

    print(min_val)

main()
'''
    if min_val == val:
        print('ok')
    else:
        print(val)
        print(A_c,L,R)
'''

    