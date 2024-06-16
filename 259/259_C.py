
S = input()
T = input()

S_press = [[S[0],1]]
T_press = [[T[0],1]]

for i in range(1,len(S)):
    if S[i] == S_press[-1][0]:
        S_press[-1][1] += 1
    else:
        S_press.append([S[i],1])


for i in range(1,len(T)):
    if T[i] == T_press[-1][0]:
        T_press[-1][1] += 1
    else:
        T_press.append([T[i],1])


if len(S_press) == len(T_press):
    frag = True
    for i in range(len(S_press)):
        #print(S_press[i],T_press[i])
        if S_press[i][0] == T_press[i][0] and (S_press[i][1]==T_press[i][1] or 2<=S_press[i][1]<=T_press[i][1]):
            continue
        else:
            frag = False
            break
    
    if frag == True:
        print('Yes')
    else:
        print('No')
else:
    print('No')