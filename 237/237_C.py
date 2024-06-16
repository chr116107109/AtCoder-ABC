import sys

S = input()

frag = 0
N = len(S)
for i in range(N//2):
    if not S[i] == S[N-i-1]:
        frag = 1
        break
    
if frag == 0:
    print('Yes')
    sys.exit()

back_a = 0
fora_a = 0
for i in range(N):
    if S[N-1-i] == 'a':
        back_a += 1
    else:
        break

for i in range(N):
    if S[i] == 'a':
        fora_a += 1
    else:
        break


S = ('a' * (back_a - fora_a)) + S

N = len(S)
frag = 0
for i in range(N//2):
    if not S[i] == S[N-i-1]:
        frag = 1
        break


if frag == 1 :
    print('No')
else:
    print('Yes')