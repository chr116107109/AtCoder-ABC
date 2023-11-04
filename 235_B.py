
N = int(input())
H = list(map(int,input().split()))

now = H[0]
for i in range(1,N):
    if now < H[i]:
        now = H[i]
    else:
        break


print(now)
