
N = int(input())

s = []
for i in range(2,N+1):
    if i**2 > N:
        break
    s.append(i**2)

ans = {(1,1)}
for i in range(1,N+1):
    x = i
    for k in s:
        #print(i,x)
        if x < k:
            break
        while x%k == 0:
            x = x//k
    #print(i,x)
    ans.add((i,x))
    ans.add((x,i))
    for l in s:
        if x*l <= N:
            ans.add((i,x*l))
            ans.add((x*l,i))

print(len(ans))
#ans = list(ans)
#ans.sort(key=lambda x:10**10*x[0]+x[1])
import itertools

def is_squere(N):
    for i in range(N+1):
        if i*i > N:
            break
        if i*i == N:
            return True
    return False
def naive(N):
    ans = set()
    for i,j in itertools.product(range(1,N+1),range(1,N+1)):
        if is_squere(i*j):
            ans.add((i,j))
    ans = list(ans)
    ans.sort(key=lambda x:10**10*x[0]+x[1])
    return ans