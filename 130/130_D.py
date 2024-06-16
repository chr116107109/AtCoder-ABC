

N,K = map(int,input().split())
A = list(map(int,input().split()))


B = [0]
ans = 0
import bisect
for i in range(N):
    B.append(B[-1]+A[i])

    if B[-1] >= K:
        ind = bisect.bisect_right(B,B[-1]-K)

        ans += ind


print(ans)