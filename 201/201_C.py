

S = input()

ans = 0
for i in range(10000):
    t = str(i)
    t = '0'*(4-len(t)) + t
    flag = True
    #print(t)
    for j in range(10):
        if S[j] == 'o' and (not str(j) in t):
            flag = False
            break
        elif S[j] == 'x' and (str(j) in t):
            flag = False
            break

    if flag:
        ans += 1

print(ans)