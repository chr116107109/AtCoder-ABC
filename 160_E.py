
X,Y,A,B,C = map(int,input().split())
P = list(map(int,input().split()))
Q = list(map(int,input().split()))
R = list(map(int,input().split()))

q = []
for i in range(A):
    q.append([P[i], 'r'])
for i in range(B):
    q.append([Q[i], 'b'])
for i in range(C):
    q.append([R[i], 'w'])

q.sort(key=lambda x:x[0])

Z_R = 0
Z_B = 0
ans = 0
while q:
    #print(q,ans)
    v,c = q.pop()
    #print(X,Y,Z)
    if c == 'r':
        if X == 0 and Z_R > 0 and Y > 0:
            Z_R -= 1
            Y -= 1
            ans += v
        elif X > 0:
            X -= 1
            ans += v
    if c == 'b':
        if Y == 0 and Z_B > 0 and X > 0:
            Z_B -= 1
            X -= 1
            ans += v
        elif Y > 0:
            Y -= 1
            ans += v
    if c == 'w':
        if X > 0:
            Z_R += 1
            X -= 1
            ans += v
        elif Y > 0:
            Z_B += 1
            Y -= 1
            ans += v

print(ans)