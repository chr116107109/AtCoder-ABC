
N = int(input())


def main(N):
    i = 1
    ans = 0
    while i <= N**(0.5):
        a = N//i
        b = (N//a)
        m = (a-N//(i+1))
        #print(i,a,b,m)
        ans += a
        if a != b:
            ans += b*m
        i += 1
    return ans
def naive(N):
    ans = 0
    for i in range(1,N+1):
        ans += N//i

    return ans

print(main(N))