
N = int(input())
A = list(map(int,input().split()))
Q = int(input())
iregular = {}
for i in range(N):
    iregular[i+1] = A[i]

other = 0
ans = []
for _ in range(Q):
    q = list(map(int,input().split()))
    if q[0] == 1:
        iregular = {}
        other = q[1]
    if q[0] == 2:
        [i,x] = q[1:]
        if i in iregular:
            iregular[i] += x
        else:
            iregular[i] = other + x
    if q[0] == 3:
        i = q[1]
        if i in iregular:
            ans.append(iregular[i])
            #print(iregular[i])
        else:
            ans.append(other)
            #print(other)

for a in ans:
    print(a)