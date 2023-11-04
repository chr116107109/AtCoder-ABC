
N = int(input())
S = input()

ind = []

for i in range(N):
    if S[i] == '|':
        ind.append(i)

if ind[0] < S.index('*') < ind[1]:
    print('in')
else:
    print('out')