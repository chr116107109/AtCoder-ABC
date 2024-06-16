

N = int(input())
Q = int(input())
card = [[] for i in range(N)]
box = {}
for i in range(Q):
    q = list(map(int,input().split()))

    if q[0] == 1:
        i,j = q[1]-1,q[2]-1
        card[j].append(i+1)
        if i in box:
            box[i].add(j+1)
        else:
            box[i] = {j+1}
    if q[0] == 2:
        i = q[1]-1
        print(*sorted(card[i]))
    if q[0] == 3:
        i = q[1] - 1
        print(*sorted(box[i]))
