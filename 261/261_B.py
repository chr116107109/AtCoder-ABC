
N = int(input())
A = [input() for i in range(N)]

ans = 'correct'
for i in range(N):
    for j in range(N):
        if i == j:
            continue
        if A[i][j] == 'W' and A[j][i] == 'L':
            continue
        elif A[i][j] == 'L' and A[j][i] == 'W':
            continue
        elif A[i][j] == 'D' and A[j][i] == 'D':
            continue
        else:
            ans = 'incorrect'

print(ans)        
        
