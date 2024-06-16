
N,Q = map(int,input().split())

yellow = [0] * N
banned = set()
for i in range(Q):
    q = list(map(int,input().split()))
    if q[0] == 1:
        yellow[q[1]-1] += 1
        if yellow[q[1]-1] > 1:
            banned.add(q[1])
    if q[0] == 2:
        banned.add(q[1])
    if q[0] == 3:
        if q[1] in banned:
            print('Yes')
        else:
            print('No')