
[N,M] = list(map(int,input().split()))
AB = [list(map(int,input().split())) for i in range(M)]
CD = [list(map(int,input().split())) for i in range(M)]

import itertools
import copy
frag = 0
for v in itertools.permutations(list(range(1,N+1)), N):
    E = copy.deepcopy(AB)
    #print(v)
    for i in range(M):
        f = sorted([v[CD[i][0]-1],v[CD[i][1]-1]])
        if f in E:
            E.remove(f)
        #print(E)

    if E == []:
        frag = 1
        break


if frag ==1 :
    print('Yes')
else:
    print('No')
