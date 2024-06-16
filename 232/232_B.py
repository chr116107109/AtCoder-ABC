
S = input()
T = input()
frag = 0

for i in range(30):
    ans = ''
    for j in range(len(S)):
        ans += chr(ord('a')+(ord(S[j])-ord('a')+i)%26)

    if ans == T :
        frag = 1

    #print(ans)


if frag == 1:
    print('Yes')
else:
    print('No')
