

N = int(input())
S = input()


def h(s,mod1,mod2):
    t = s[::-1]
    re = 0
    for i in range(len(t)):
        re += pow(mod2,i)*ord(t[i])
        re %= mod1
    return re
def RolingHash(S,n, mod1, mod2):

    def f(c):
        return (ord(c))
    A = {}
    p = 1
    hash = 0
    for i in range(n-1,-1,-1):
        hash += p*f(S[i])
        hash %= mod1
        p *= mod2
    A[hash] = 0
    for i in range(1,N-n+1):
        hash *= mod2
        hash -= p*f(S[i-1])
        hash += f(S[i+n-1])
        hash %= mod1
        #print(i,hash, S[i:i+n])
        if not hash in A:
            A[hash] = i
        elif A[hash] <= i-n:
            #print(A[hash],S[i:i+n])
            return True
        
    return False



left = 0
right = N
mod1 = 871661229453823
mod2 = 10**7+9
mod3 = 10**7
mod4 = 692017 

while left < right:
    #print(left,right)
    m = (left+right)//2
    d = {}
    
    if RolingHash(S,m,mod1,mod2):
        left = m+1
    else:
        right = m

print(max(left-1,0))