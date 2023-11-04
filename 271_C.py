
N = int(input())
A = list(map(int,input().split()))

Aset = set(A)
left = 0
right = len(A)
while left < right-1:
    #print(left,right)
    m = (left + right)//2
    n_delete = 0
    for i in range(1,m+1):
        if i in Aset:
            n_delete += 1
        else:
            n_delete += 2

    if n_delete > N:
        right = m - 1
    else:
        left = m

n_delete = 0
for i in range(1,right+1):
    if i in Aset:
        n_delete += 1
    else:
        n_delete += 2

if n_delete > N:
    print(left)
else:
    print(right)