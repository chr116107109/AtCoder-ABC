
N = int(input())
S = input()
Q = int(input())


T = [list(S[:N]), list(S[N:])]
now = 0
for i in range(Q):
    I,A,B = map(int,input().split())

    if I == 1:
        if A < B <= N:
            T[now][A-1], T[now][B-1] = T[now][B-1], T[now][A-1]
        elif N < A < B:
            A -= N
            B -= N
            T[(now+1)%2][A-1], T[(now+1)%2][B-1] = T[(now+1)%2][B-1], T[(now+1)%2][A-1]
        else:
            T[now][A-1], T[(now+1)%2][B-N-1] = T[(now+1)%2][B-N-1], T[now][A-1]

    if I == 2:
        now = (now+1)%2


print("".join(T[now]+T[(now+1)%2]))

