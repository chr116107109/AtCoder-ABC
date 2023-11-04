

S = input()

old2019 = [0] * 2019
new2019 = [0] * 2019
old2019[int(S[0])] += 1
N = len(S)
ans = 0
for i in range(1,N):

    n = int(S[i])
    for j in range(2019):
        new2019[(10*j+n)%2019] += old2019[j]
    new2019[int(S[i])] += 1
    ans += new2019[0]

    
    old2019 = new2019[:]
    new2019 = [0]*2019

print(ans)