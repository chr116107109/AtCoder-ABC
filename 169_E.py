
N = int(input())
A = [list(map(int,input().split())) for i in range(N)]

B = []
for i in range(N):
    B.append([A[i][0],'L'])
    B.append([A[i][1],'R'])

B.sort(key=lambda x:x[0])
if N%2 == 0:
    count_l = 0 
    count_r = 0
    L = [0,0]
    R = [0,0]
    for i in range(2*N):
        if B[i][1] == 'L':
            count_l += 1
            if count_l == N//2:
                L[0] = B[i][0]
            if count_l == N//2+1:
                R[0] = B[i][0]
        if B[i][1] == 'R':
            count_r += 1
            if count_r == N//2:
                L[1] = B[i][0]
            if count_r == N//2+1:
                R[1] = B[i][0]

    print(L[1] + R[1] - L[0] - R[0] + 1)

else:
    count_l = 0 
    count_r = 0
    for i in range(2*N):
        if B[i][1] == 'L':
            count_l += 1
            if count_l == N//2+1:
                L = B[i][0]
        if B[i][1] == 'R':
            count_r += 1
            if count_r == N//2+1:
                R = B[i][0]

    print(R-L+1)