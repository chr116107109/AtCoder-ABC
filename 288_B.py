
N,K = map(int,input().split())
S = [input() for i in range(N)]

T = sorted(S[:K])

for i in range(K):
    print(T[i])