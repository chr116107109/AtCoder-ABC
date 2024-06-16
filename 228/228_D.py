
Q = int(input())

N = 10

def find(p,h):
    if p[h] == -1:
        return h

    else:
        p[h] = find(p,p[h])
        return p[h]

def union(p,a,b):
    fa = find(p,a)
    fb = find(p,b)

    if fa == fb:
        return

    p[fa] = fb


p = [-1] * N
# pは根

A = [-1] * N
#ans


for i in range(Q):
    [t,x] = list(map(int,input().split()))

    if t == 1:
        h = x
        h = h%N
        if A[h] == -1:
            A[h] = x
            if A[(h-1)%N] > -1:
                union(p,(h-1)%N,h)

            if A[(h+1)%N] > -1:
                union(p,h,(h+1)%N)


        else:
            h = find(p,h)
            A[(h+1)%N] = x
            union(p,h,(h+1)%N)

            if A[(h+2)%N] > -1:
                union(p,h,(h+2)%N)



        print(p)
        print(A)

    if t == 2:
        h = x%N
        #h = find(p,h)
        print(A[h])
