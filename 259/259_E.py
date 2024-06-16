

N = int(input())
primes = set()
A = [{} for i in range(N)]
for i in range(N):
    m = int(input())
    for _ in range(m):
        p,e = map(int,input().split())
        A[i][p] = e
        primes.add(p)

M = len(primes)
primes_to_ind = {}
for i,p in enumerate(primes):
    primes_to_ind[p] = i

d = [{} for i in range(M)]
maxe = [0] * M
for i in range(N):
    for p in A[i]:
        e = A[i][p]
        if e in d[primes_to_ind[p]]:
            d[primes_to_ind[p]][e] += 1
        else:
            d[primes_to_ind[p]][e] = 1
        maxe[primes_to_ind[p]] = max(maxe[primes_to_ind[p]], e)

ans = 1

for i in range(N):
    #print('left',left)
    #rprint(A[i],ans)
    #print('right',d[i])    
    for p in A[i]:
        e = A[i][p]
        if d[primes_to_ind[p]][e] == 1 and maxe[primes_to_ind[p]] == e:
            ans += 1
            break


print(min(ans,N))