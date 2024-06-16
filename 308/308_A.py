
S =  list(map(int,input().split()))

ans = 'Yes'
for i in range(8):
    if not 100 <= S[i] <= 675:
        ans = 'No'
    if i < 7 and (not (i < 7 and S[i] <= S[i+1])):
        ans = 'No'
    if not (S[i]%25 == 0):
        ans = 'No'

print(ans)