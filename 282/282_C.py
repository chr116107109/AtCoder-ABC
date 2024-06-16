
N = int(input())
S = list(input())

M = 0

for i in range(N):
    if S[i] == ',':
        if M%2 == 0:
            S[i] = '.'
    if S[i] == '"':
        M += 1

print("".join(S))