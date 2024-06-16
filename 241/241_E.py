
N,K = map(int,input().split())
A = list(map(int,input().split()))

roop = {}
now = 0 
num = 0
X = 0
while not now in roop:
    roop[now] = num
    X += A[now]
    num += 1
    now = X%N

n_before_roop = roop[now]
n_roop = len(roop) - n_before_roop
before_roop = []
sum_roop = 0
for i in roop:
    if roop[i] < n_before_roop:
        before_roop.append(roop[i])
    else:
        sum_roop += A[i]
X = 0
if K < n_before_roop:
    ans = 0
    X = 0
    for i in range(K):
        X += A[X%N]
    print(X)
else:
    for i in range(n_before_roop):
        X += A[X%N]
    #print(X,K)
    K -= n_before_roop
    X += sum_roop*(K//n_roop)
    K %= n_roop
    #print(X,K)
    for i in range(K):
        X += A[X%N]
    print(X)