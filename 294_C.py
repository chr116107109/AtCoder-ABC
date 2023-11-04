

N,M = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

AA = [[A[i],'A'] for i in range(N)]
BB = [[B[i],'B'] for i in range(M)]

a = 1
b = 1

C = AA + BB
C.sort(key=lambda x:x[0])

ansA = []
ansB = []
for i in range(N+M):
    if C[i][1] == 'A':
        ansA.append(i+1)
        a += 1
    else:
        ansB.append(i+1)
        b += 1

print(*ansA)
print(*ansB)
