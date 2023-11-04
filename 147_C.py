
N = int(input())

A = []
for i in range(N):
    A.append([])
    n = int(input())
    for j in range(n):
        A[-1].append(list(map(int,input().split())))

ans = 0
for bit in range(2**N):
    count = 0
    ok = True
    for i in range(N):
        if bit&(1<<i) != 0:
            count += 1
            for x,y in A[i]:
                if (bit&(1<<(x-1)) != 0 and y==1) or (bit&(1<<(x-1)) == 0 and y==0):
                    continue
                ok = False
                break
    if ok:
        ans = max(count,ans)

print(ans)