
S = sorted(set(input()))

L = list(input().split())

A = set()
for t in L:
    #print(sorted(set(t)))
    if sorted(set(t)) == S:
        print(t)
        print('same')
        A.add(t)

print(len(A))