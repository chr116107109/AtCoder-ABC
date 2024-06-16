
S = input()

minS = S
maxS = S
for i in range(len(S)):
    S = S[1:] + S[:1]
    if S > maxS:
        maxS = S
    if S < minS:
        minS = S

print(minS)
print(maxS)
