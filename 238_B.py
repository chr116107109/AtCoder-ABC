
N = int(input())

A = list(map(int,input().split()))

R = [360]
s = 0
for a in A:
    s = (s+a) % 360

    t = 0
    for i in range(len(R)):
        t += R[i]
        if t > s or i == len(R)-1:
            R.insert(i,R[i]-(t-s))
            R[i+1] = R[i+1] - R[i]
            break
    #print(R)


print(max(R))




