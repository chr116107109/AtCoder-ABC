
N = int(input())

i = 1
ans = 10
while i <= N**(1/2):
    if N%i == 0:
        ans = len(str(N//i))
    i += 1

print(ans)