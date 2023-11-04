
A = list(map(int,input().split()))



if len(set(A)) == 2 and (len([a for a in A if a == A[0]]) == 3 or len([a for a in A if a == A[0]]) == 2):
    print('Yes')
else:
    print('No')