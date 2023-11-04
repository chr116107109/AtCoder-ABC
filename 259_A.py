
N,M,X,T,D = map(int,input().split())

S = 0
if N <= X:
    S = T - N*D
else:
    S = T - X*D

if M <= X:
    print(S+D*M)
else:
    print(S+D*X)