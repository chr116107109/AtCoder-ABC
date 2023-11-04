

N,K = map(int,input().split())

for i in range(K):
    if N%200 == 0:
        N //= 200
    else:
        n=str(N)
        N = int(n+'200')

print(N)