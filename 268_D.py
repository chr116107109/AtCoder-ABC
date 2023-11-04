

N,M = map(int,input().split())
S = [input() for i in range(N)]
T = {input() for i in range(M)}

from collections import deque
import itertools
def insert_bar(N,possible_bar):
    if possible_bar == 0:
        return []
    paths = set()
    queue =  deque()
    queue.append(('0',0))
    visited = set()
    while queue:
        #print(queue)
        path, n_bar = queue.popleft()
        if path in visited:
            continue
        visited.add(path)
        paths.add(path+('0'*(N-len(path))))
        if n_bar < possible_bar:
            queue.append((path[:-1]+str(int(path[-1])+1), n_bar+1))
            if len(path) < N:
                queue.append((path+'0',n_bar))
                queue.append((path+'1',n_bar+1))
    return paths
def make_pass(perm_S,p):
    pas = perm_S[0]
    for i in range(len(perm_S)-1):
        pas += '_' * (1+int(p[i])) + perm_S[i+1]
    return pas




possible_bar = 16 - (len(S)-1) - sum([len(s) for s in S])
if possible_bar >0:
    paths = insert_bar(N-1,possible_bar)
else:
    paths = ['0'*(N-1)]
ans = -1
for perm_S in itertools.permutations(S):
    for p in paths:
        pas = make_pass(perm_S,p)
        #print(pas)
        if (not pas in T) and 16>=len(pas) >= 3:
            ans = pas
            

print(ans)


