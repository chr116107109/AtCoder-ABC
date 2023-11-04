

N,M = map(int,input().split())

ori = M

p = set()
for i in range(1,int(M**(0.5))+1):
    if M%i == 0:
        p.add(i)
        p.add(M//i)

ans = min([i for i in p if i >= N])
    
print(ori//ans)