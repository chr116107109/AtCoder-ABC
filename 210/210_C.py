import numpy as np

[N, K] = list(map(int, input().split()))
c = list(map(int, input().split()))

c = np.array(c)

sub_c = c[0:K]
u,counts = np.unique(sub_c,return_counts=True)

color_dict = dict(zip(u,counts))

ans = len(u)

#print(color_dict)

for i in range(1,N-K+1):

    if color_dict[c[i-1]]==1:
        del(color_dict[c[i-1]])
    else:
        color_dict[c[i-1]] = color_dict[c[i-1]]-1

    if c[i+K-1] in color_dict:
        color_dict[c[i+K-1]] = color_dict[c[i+K-1]]+1
    else:
        color_dict[c[i+K-1]] = 1

    sub_ans = len(color_dict)

    #print(color_dict)
    #print(c[i:i+K-1])
    #print(sub_ans,ans)
    ans = max([ans,sub_ans])

print(ans)
