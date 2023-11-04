
import collections

N = int(input())

S = [input() for i in range(N)]

A = collections.Counter(S)

print(A.most_common()[0][0])
