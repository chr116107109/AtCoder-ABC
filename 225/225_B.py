import sys

N = int(input())

ab = [list(map(int,input().split())) for i in range(N-1)]


d = [[i+1,[]] for i in range(N)]

for i in range(N-1):
    d[ab[i][0]-1][1] += [ab[i][1]]
    d[ab[i][1]-1][1] += [ab[i][0]]

if len(d[ab[0][0]-1][1]) < N-1 and len(d[ab[0][1]-1][1]) < N-1:
    print('No')
    sys.exit()

for a in [ab[0][0],ab[0][1]]:
    sortd = sorted(d[a-1][1])
    ans = list(range(1,N+1))
    ans.remove(a)
    if sortd == ans:
        print('Yes')
        sys.exit()

print('No')
