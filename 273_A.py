
N = int(input())

def frac(N):
    if N == 0:
        return 1
    return N*frac(N-1)

print(frac(N))