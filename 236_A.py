
S = list(input())
[a,b] = map(int,input().split())

Sa = S[a-1]
Sb = S[b-1]

S[a-1] = Sb
S[b-1] = Sa


print(*S, sep='')
