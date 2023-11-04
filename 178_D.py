

S = int(input())
P = 10**9 + 7
d = [[0]*(S) for i in range(S//3)]
com = [0] * (S+1)

for i in range(2,S):
    d[0][i] = 1
    com[i+1] = com[i] + d[0][i] 

for i in range(1,S//3):
    #print(com)
    for j in range((i+1)*3-1,S):
        d[i][j] = com[j-2]
    for j in range(1,S+1):
        com[j] = (com[j-1] + d[i][j-1])%P


ans = 0
for i in range(S//3):
    ans = (ans + d[i][S-1])%P

print(ans)
