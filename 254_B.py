
N = int(input())

for i in range(N):
    a = [1] * (i+1)
    for j in range(1,i):
        a[j] = a_old[j-1] + a_old[j]
    print(*a)
    a_old = a


