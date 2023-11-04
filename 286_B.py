
N = int(input())
S = list(input())

T = []
S = S[::-1]
now = ''
while S:
    now = S.pop()
    T.append(now)
    if S == []:
        break
    if now == 'n' and S[-1] == 'a':
        T.append('y')

print("".join(T))