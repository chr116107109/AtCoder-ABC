
import itertools


N = int(input())
A = [list(map(int,input().split())) for i in range(N)]

ans = 0
for [t1,l1,r1],[t2,l2,r2] in itertools.combinations(A,2):
    if min(r1,r2) > max(l1,l2):
        ans += 1
    elif l1 == r2 and (t1 == 1 or t1==2) and (t2 == 1 or t2==3):
        ans += 1
    elif l2 == r1 and (t1 == 1 or t1==3) and (t2 == 1 or t2==2):
        #print([t1,l1,r1],[t2,l2,r2],ans)
        ans += 1

print(ans)