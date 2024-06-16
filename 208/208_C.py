import numpy as np

[N, K] = list(map(int, input().split()))
a = list(map(int, input().split()))
a = np.array(a)

onaji = K//N
amari = K%N

arg_a = np.argsort(a)

ans = [onaji] * N
for i in range(amari):
    ans[arg_a[i]] = ans[arg_a[i]] + 1
#print(arg_a)

for i in range(N):
    print(ans[i])
