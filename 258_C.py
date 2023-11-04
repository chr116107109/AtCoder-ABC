
N,Q = map(int,input().split())
S = input()

now = 0
for i in range(Q):
    q = list(map(int,input().split()))

    if q[0] == 1:
        now = (now - q[1])%N
    elif q[0] == 2:
        print(S[(now+q[1]-1)%N])
