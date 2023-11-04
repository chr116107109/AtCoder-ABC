
import itertools
N,A,B,C = map(int,input().split())

L = [int(input()) for i in range(N)]

ans = 10**10
for p in itertools.permutations(L):
    p = list(p)
    for w in itertools.combinations(range(N+1),3):
        w = sorted(list(w))
        a = p[:w[0]]
        b = p[w[0]:w[1]]
        c = p[w[1]:w[2]]
        #print(a)

        if a == [] or b == [] or c == []:
            continue

        score = 10*((len(a)-1)+(len(b)-1)+(len(c)-1))
        score += abs(A-sum(a))
        score += abs(B-sum(b))
        score += abs(C-sum(c))

        ans = min(ans,score)

print(ans)