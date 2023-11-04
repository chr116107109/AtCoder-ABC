

N = int(input())
S = str(input())


for i in range(N):
    if S[i]=='1':
        number = i
        break

if number%2 == 1:
    print("Aoki")
else:
    print("Takahashi")
