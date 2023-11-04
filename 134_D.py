
N = int(input())
a = list(map(int,input().split()))

box = [0] * N
ans = []
for i in range(N-1,-1,-1):
    j = i + 1
    part_sum = 0
    k = 2
    j *= k
    while j <= N:
        #print(j)
        part_sum += box[j-1]
        j += (i+1)
        k += 1
    
    box[i] = (a[i] - part_sum)%2
    if box[i] == 1:
        ans.append(i+1)
    #print(part_sum)
    #print(box)

ans.reverse()
print(len(ans))
print(*ans)