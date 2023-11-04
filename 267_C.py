
N,M = map(int,input().split())
A = list(map(int,input().split()))


part_sum = [0] * (N-M+1)
part_sum[0] = sum(A[:M])
for i in range(1,N-M+1):
    part_sum[i] = part_sum[i-1] + A[M-1+i] - A[i-1]

def naive(s,A,M):
    part = 0
    for i in range(M):
        part += (i+1) * A[i+s]
    return part

part = 0
for i in range(M):
    part += (i+1) * A[i]

ans = part

for i in range(1,N-M+1):
    part = part - part_sum[i-1] + M*A[M-1+i]
    #print(part,naive(i,A,M))
    ans = max(part,ans)

print(ans)