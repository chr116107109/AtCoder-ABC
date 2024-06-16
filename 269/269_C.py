
N = int(input())
binN = list(bin(N)[2:])
binN.reverse()

from collections import deque
ans = deque()
for i in range(len(binN)):
    if binN[i] == '1':
        if len(ans) == 0:
            ans.append('0'+('0'*i))
            ans.append('1'+('0'*i))
        else:
            for j in range(len(ans)):
                a = ans.popleft()
                ans.append('0'+a)
                ans.append('1'+a)
    else:
        for j in range(len(ans)):
            a = ans.popleft()
            ans.append('0' + a)
    #print(ans)

ANS = []
for i in range(len(ans)):
    a = ans.popleft()
    ANS.append(int(a,2))

ANS.sort()

for a in ANS:
    print(a)

if ANS == []:
    print(0)