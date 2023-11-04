
N = int(input())
S = input()

A = [{} for i in range(N+1)]
A[0]['R'] = 0
A[0]['G'] = 0
A[0]['B'] = 0
for i in range(N):
    A[i+1]['R'] = A[i]['R']
    A[i+1]['G'] = A[i]['G']
    A[i+1]['B'] = A[i]['B']
    A[i+1][S[i]] += 1

ans = 0
for i in range(N-2):
    M = 1
    for c in {'R','G','B'} - {S[i]}:
        M *= A[-1][c] - A[i][c]

    for j in range(i+1,N):
        if j+(j-i) > N-1:
            continue
        if {S[i], S[j], S[j+(j-i)]} == {'R','G','B'}:
            M -= 1
    ans += M
print(ans)