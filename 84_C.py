
N = int(input())

time = [0] * N

for i in range(N-1):
    C,S,F = map(int,input().split())

    time[i] = S + C
    for j in range(i):
        if time[j] < S:
            time[j] = S + C
        else:
            time[j] += (-time[j])%F + C

for i in range(N):
    print(time[i])