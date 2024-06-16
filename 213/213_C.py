

[H,W,N] = list(map(int, input().split()))

cards = []
for i in range(N):
    A,B = map(int,input().split())
    cards.append((A,B,i))

ans = [[-1,-1] for i in range(N)]

order = {x[0] for x in cards}
order = sorted(list(order))
d = {}
for i,x in enumerate(order):
    d[x] = i
for i in range(N):
    A,B,ind = cards[i]
    ans[ind][0] = d[A]+1


order = {x[1] for x in cards}
order = sorted(list(order))
d = {}
for i,x in sorted(enumerate(order)):
    d[x] = i
for i in range(N):
    A,B,ind = cards[i]
    ans[ind][1] = d[B] + 1

for i in range(N):
    print(*ans[i])