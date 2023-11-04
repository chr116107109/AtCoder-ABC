
N = int(input())
S = input()

red = [0] * (N+1)
white = [0] * (N+1)

for i in range(N):
    red[i+1] = red[i]
    white[i+1] = white[i]
    if S[i] == 'W':
        white[i+1] += 1
    else:
        red[i+1] += 1

for i in range(N+1):
    if white[i] == red[-1] - red[i]:
        print(white[i])