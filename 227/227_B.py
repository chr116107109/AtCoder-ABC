
N = int(input())
S = list(map(int,input().split()))


for a in range(1,150):
    for b in range(1,150):
        if 4*a*b + 3*a + 3*b <= 1000:
            T = 4*a*b + 3*a + 3*b
            for j in range(30):
                if T in S:
                    S.remove(T)
                else:
                    break


print(len(S))
