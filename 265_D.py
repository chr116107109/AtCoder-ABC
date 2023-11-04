
#N,P,Q,R = map(int,input().split())
#A = list(map(int,input().split()))

import random


from collections import deque
def syakutori(A,P,start):
    q = deque()
    part_sum = 0
    left = start 
    right = start
    LRset = []
    for c in A[start:]:
        if part_sum == P:
            LRset.append([left,right])
        q.append(c)  ## dequeの右端に要素を一つ追加する。
        part_sum += c
        right += 1
        #print(q,part_sum,[left,right])

        while not (part_sum <= P):
            rm = q.popleft() ## 条件を満たさないのでdequeの左端から要素を取り除く
            part_sum -= rm
            left += 1
    return LRset

def main(N,P,Q,R,A):
    d = syakutori(A,P+Q+R,0)
    flag = 0
    for [left,right] in d:
        part_sum = 0
        l,r = left,right
        while part_sum < P:
            part_sum += A[l]
            l += 1
            #print(part_sum)
        
        if part_sum == P:
            while part_sum < P+Q:
                part_sum += A[l]
                l += 1
            if part_sum == P+Q:
                flag = 1
                
        if flag == 1:
            break

    #if flag == 1:
    #    print('Yes')
    #else:
    #    print('No')
    
    return flag

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
            if ruiseki[min(b,N-2)] == Q+ruiseki[a]:
                c = bin_search(ruiseki,R+ruiseki[b],b+1)
                #print('c',c,ruiseki[c+b+a+i+1] - ruiseki[b+a+i+1])
                if ruiseki[min(c,N-1)] == R + ruiseki[b]:
                    frag = 1
        
        if frag == True:
            break

    #if frag == 1:
    #    print('Yes')
    #else:
    #    print('No')
    
    return frag


def test():
    N = 10000
    P = random.randint(1,100)
    Q = random.randint(1,100)
    R = random.randint(1,100)
    A = [random.randint(1,10) for i in range(N)]

    if exact(N,P,Q,R,A) == main(N,P,Q,R,A):
        #print('ok')
        return True
    else:
        print(A)
        return False