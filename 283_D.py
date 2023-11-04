
S = input()

d = [set()]
allset = set()
deep = 0
N = len(S)
ans = 'Yes'
for i in range(N):
    if S[i] == '(':
        deep += 1
        if len(d) <= deep:
            d.append(set())
    elif S[i] == ')':
        for t in d[deep]:
            allset.remove(t)
        d[deep] = set()
        deep -= 1
    else:
        if S[i] in allset:
            ans = 'No'
            break
        d[deep].add(S[i])
        allset.add(S[i])
    #print(deep,d)

print(ans)