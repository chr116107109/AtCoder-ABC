

N,P,Q,R = map(int,input().split())
A = list(map(int,input().split()))

def bin_search(A,X,start):
    left = start
    right = len(A)-1
    while left < right:
        m = (left+right)//2
        if A[m] < X:
            left = m + 1
        else:
            right = m
    
    return left

def exact(N,P,Q,R,A):
    ruiseki = [0] * (N+1)
    for i in range(N):
        ruiseki[i+1] = ruiseki[i] + A[i]

    frag = 0
    for i in range(N+1-3):
        a = bin_search(ruiseki,P+ruiseki[i],i)
        #print('a',a,ruiseki[a+i]-ruiseki[i])
        if ruiseki[a] == P+ruiseki[i]:
            b = bin_search(ruiseki,Q+ruiseki[a],a+1)
            #print('b',b,ruiseki[b+a+i+1]-ruiseki[a+i])
            if ruiseki[b] == Q+ruiseki[a]:
                c = bin_search(ruiseki,R+ruiseki[b],b+1)
                #print('c',c,ruiseki[c+b+a+i+1] - ruiseki[b+a+i+1])
                if ruiseki[c] == R + ruiseki[b]:
                    frag = 1
        
        if frag == True:
            break

    if frag == 1:
        print('Yes')
    else:
        print('No')
    
    return frag
