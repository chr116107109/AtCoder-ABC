
[N,M] = list(map(int,input().split()))
A = list(map(int,input().split()))
B = list(map(int,input().split()))

frag = 0
for i in range(M):
    if B[i] in A:
        A.remove(B[i])
    else:
        frag = 1
        break

if frag == 1:
    print('No')
else:
    print('Yes')
