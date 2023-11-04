
N = int(input())
S = input()

ans = 0
for i in range(1,N):
    l = 0
    while S[l] != S[i+l]:
        l += 1
        if i+l > N-1:
            break

    print(l)