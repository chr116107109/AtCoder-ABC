
N = int(input())

D = set()

point = 0
ans = 0 
for i in range(N):
    S,T = input().split()
    T = int(T)
    if T > point and (not S in D):
        point = T
        ans = i+1
    D.add(S)

print(ans)

