
X = input()
A = [int(x) for x in X]
N = len(A)
comm = [0] * (N+1)
for i in range(1,N+1):
    comm[i] = comm[i-1] + A[i-1]

ans = []

v = 0
for i in range(N,-1,-1):
    v += comm[i]
    if i == 0 and v == 0:
        break
    ans.append(str(v%10))
    v //= 10

print("".join(ans[::-1]))