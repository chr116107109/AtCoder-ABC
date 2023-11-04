
N = int(input())

ans = []
for i in range(120):
    #print(N)
    if N%2 == 0:
        N = N//2
        ans.insert(0,'B')
    else:
        N = N - 1
        ans.insert(0,'A')

    if N == 0:
        break

print(*ans,sep = '')
