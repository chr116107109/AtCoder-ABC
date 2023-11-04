

[A,B] = list(map(int, input().split()))

ans = bin(A^B)

#print(bin(A))
#print(bin(B))
#print(ans)
print(int(ans,2))
