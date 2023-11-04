

N = int(input())

ans = N//100+1
if N%100==0:
    ans-=1
print(ans)