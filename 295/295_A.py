

N = int(input())
ans = 'No'
W = list(input().split())
for i in range(N):

    if W[i] in ['and', 'not', 'that', 'the', 'you']:
        ans = 'Yes'
    
print(ans)