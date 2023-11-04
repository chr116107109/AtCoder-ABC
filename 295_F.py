
T = int(input())

for i in range(T):
    S,L,R = input().split()
    n = max(len(L),len(R))
    L = '0'*(n-len(L)) + L
    m = len(S)
    for j in range(n-m):
        if S < L[-m-j:]:
            botom = str(int(L[-m-j-1])+1) + S
        else:
            botom = S + '0'*j
        
        if S > R[-len(S):]:
            up = str(int(L[-m-j-1])-1) + S
        else:
            up = S + '9'*j