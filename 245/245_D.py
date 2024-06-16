
N,M = map(int,input().split())
A = list(map(int,input().split()))
C = list(map(int,input().split()))


def main(A,C,M,N):
    A.reverse()
    A = A + ([0]*M)
    C.reverse()
    B = [0] * (M+1)

    for i in range(M+1):
        for b in range(-100,101):
            B[i] = b
            part_sum = 0
            for j in range(i+1):
                part_sum += A[j]*B[i-j]
            if part_sum == C[i]:
                break

    #print(*B[:M+1])
    B.reverse()
    return B[:M+1]

B = main(A,C,M,N)
print(*B)
import random
def test():
    N = 5
    M = 3
    A = [random.randint(-5,5) for _ in range(N)] + [1]
    B = [random.randint(-5,5) for _ in range(M)] + [1]
    
    C = [0] * (N+M+1)
    for i in range(N+1):
        for j in range(M+1):
            C[i+j] += A[i]*B[j]
    
    if B != main(A,C,M,N):
        print(A)
        print(B)
        print(C)