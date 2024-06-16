
[A,B,C] = list(map(int,input().split()))

m = 0
for i in range(1,2000):
    if C*i >= A and C*i <= B:
        print(C*i)
        m = 1
        break

if m == 0:
    print(-1)
