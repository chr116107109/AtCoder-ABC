

N = int(input())
A = set(map(int,input().split()))

ans = 'Yes'
for i in range(1,N+1):
    if i in A:
        continue
    else:
        ans = 'No'

print(ans)