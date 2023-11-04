import sys

S = input()

N = len(S)

T = ''
for i in range(30):
    T += 'oxx'

for i in range(5):
    if S == T[i:N+i]:
        print('Yes')
        sys.exit()


print('No')
