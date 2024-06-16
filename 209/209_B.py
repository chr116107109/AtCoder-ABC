

[N, X] = list(map(int, input().split()))
A = list(map(int, input().split()))

goukei = 0
for i in range(N):
    if (i+1)%2==1:
        goukei = goukei + A[i]
    else:
        goukei = goukei + A[i] - 1

#print(goukei)
if goukei<=X:
    print("Yes")
else:
    print("No")
