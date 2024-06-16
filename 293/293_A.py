

S = list(input())

for i in range(len(S)):
    if i%2 == 1:
        continue
    S[i],S[i+1] = S[i+1],S[i]

print(''.join(S))