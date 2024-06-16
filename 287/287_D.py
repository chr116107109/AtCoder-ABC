
S = input()
T = input()

N = len(T)
ok_forward = [0] * (N+1)
ok_forward[0] = 1
for i in range(1,N+1):
    if ok_forward[i-1] == 1 and (S[i-1] == T[i-1] or S[i-1] == '?' or T[i-1] == '?'):
        ok_forward[i] = 1

ok_backward = [0] * (N+1)
ok_backward[0] = 1
for i in range(1,N+1):
    if ok_backward[i-1] == 1 and (S[-i] == T[-i] or S[-i] == '?' or T[-i] == '?'):
        ok_backward[i] = 1

for i in range(N+1):
    if ok_forward[i] == 1 and ok_backward[N-i] == 1:
        print('Yes')
    else:
        print('No')