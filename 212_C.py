import numpy as np

[N,M] = list(map(int, input().split()))
A = np.array(list(map(int, input().split())))
B = np.array(list(map(int, input().split())))

AB = np.concatenate([A,B])

IND = np.argsort(AB)
ans = 1000000000
#print(AB)
#print(IND)
for i in range(N+M-1):
    if IND[i] <= N-1 and IND[i+1] > N-1:
            a = AB[IND[i]]
            b = AB[IND[i+1]]
            amb = abs(a-b)
            ans = min([ans,amb])

    if IND[i]> N-1 and IND[i+1]<=N-1:
            a = AB[IND[i]]
            b = AB[IND[i+1]]
            amb = abs(a-b)
            ans = min([ans,amb])

    #print(a,b,amb)

print(ans)
