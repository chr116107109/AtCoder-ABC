
N = int(input())
A = list(map(int,input().split()))

S = 4*(1+N)*N/2

print(int(S - sum(A)))