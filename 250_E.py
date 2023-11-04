
N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

d = [set() for i in range(N)] 

left = 0
right = 0
setB = set()
setA = set()
diff = set()
while right < N:
    C = set()
    new = B[right]
    setB.add(new)
    if not new in setA:
        diff.add(new)
    while left < N:
        if not A[left] in setB:
            break
        setA.add(A[left])
        if A[left] in diff:
            diff.remove(A[left])
        if diff == set():
            C.add(left)
        left += 1

    while right < N:
        if not B[right] in setB:
            break
        if diff == set():
            d[right] = C
        right += 1
    
    #print(diff)
    #print('')
    #print(left,right,setA,setB)


Q = int(input())

ans = []
for i in range(Q):
    x,y = map(int,input().split())
    if x-1 in d[y-1]:
        ans.append('Yes')
    else:
        ans.append('No')

for a in ans:
    print(a)