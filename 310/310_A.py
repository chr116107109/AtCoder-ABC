
N,P,Q = map(int,input().split())
A = list(map(int,input().split()))

print(min(P,Q+min(A)))