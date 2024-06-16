
N = int(input())
S = input()

t = 0
a = 0
mid = N//2 + N%2
for i in range(N):
    if S[i] == 'T':
        t += 1
    if S[i] == 'A':
        a += 1
    
    if t >= mid:
        print('T')
        break
    if a >= mid:
        print('A')
        break