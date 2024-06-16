
import itertools

N = int(input())
XY = [list(map(int,input().split())) for i in range(N)]


count = 0
for xy in itertools.combinations(XY,3):

    #print(xy)
    if (xy[1][1] - xy[0][1])*(xy[2][0] - xy[1][0]) == (xy[2][1] - xy[1][1]) * (xy[1][0] - xy[0][0]):
        continue
    else:
        count += 1

print(count)
