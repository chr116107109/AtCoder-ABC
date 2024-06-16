

H,W = map(int,input().split())
A = [input() for i in range(H)]
B = [[0]*W for i in range(H)]
for i in range(H):
    for j in range(W):
        if A[i][j] == '+':
            B[i][j] = 1
        else:
            B[i][j] = -1

from collections import deque
def bfs():
    q = deque()
    q.append(([H-1,W-1],0))
    inf = 10**10
    visited = [[0 for i in range(W)] for j in range(H)]
    score_1 = [[-inf for i in range(W)] for j in range(H)]
    score_2 = [[-inf for i in range(W)] for j in range(H)]
    score_1[H-1][W-1] = 0
    score_2[H-1][W-1] = 0
    while q:
        pos,dir = q.popleft()
        if visited[pos[0]][pos[1]] == 1:
            continue
        visited[pos[0]][pos[1]] = 1

        for next in [[pos[0]-1,pos[1]], [pos[0],pos[1]-1]]:
            if next[0] < 0 or next[1] < 0:
                continue
            
            if dir == 1:
                if score_1[next[0]][next[1]] == -inf and score_2[next[0]][next[1]] == -inf:
                    score_1[next[0]][next[1]] = score_1[pos[0]][pos[1]] + B[pos[0]][pos[1]]
                    score_2[next[0]][next[1]] = score_2[pos[0]][pos[1]]
                elif score_1[next[0]][next[1]]-score_2[next[0]][next[1]] < score_1[pos[0]][pos[1]] - score_2[pos[0]][pos[1]] + B[pos[0]][pos[1]]:
                    score_1[next[0]][next[1]] = score_1[pos[0]][pos[1]] + B[pos[0]][pos[1]]
                    score_2[next[0]][next[1]] = score_2[pos[0]][pos[1]]
            else:
                if score_1[next[0]][next[1]] == -inf and score_2[next[0]][next[1]] == -inf:
                    score_1[next[0]][next[1]] = score_1[pos[0]][pos[1]]
                    score_2[next[0]][next[1]] = score_2[pos[0]][pos[1]] + B[pos[0]][pos[1]]
                elif score_2[next[0]][next[1]]-score_1[next[0]][next[1]] < score_2[pos[0]][pos[1]] - score_1[pos[0]][pos[1]] + B[pos[0]][pos[1]]:
                    score_1[next[0]][next[1]] = score_1[pos[0]][pos[1]] 
                    score_2[next[0]][next[1]] = score_2[pos[0]][pos[1]] + B[pos[0]][pos[1]]
            
            q.append((next, (dir+1)%2))
            
    return score_1,score_2

score_1,score_2 = bfs()

if (H+W)%2 == 0:
    if score_1[0][0] == score_2[0][0]:
        print('Draw')
    elif score_1[0][0] < score_2[0][0]:
        print('Aoki')
    else:
        print('Takahashi')
else:
    if score_1[0][0] == score_2[0][0]:
        print('Draw')
    elif score_1[0][0] > score_2[0][0]:
        print('Aoki')
    else:
        print('Takahashi')