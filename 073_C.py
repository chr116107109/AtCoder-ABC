

N = int(input())

S = set()

for i in range(N):
    a = int(input())
    if a in S:
        S.remove(a)
    else:
        S.add(a)    


print(len(S))