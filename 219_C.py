
X = input()
N = int(input())

S = [input() for i in range(N)]

def hikaku(a,b,X):
    minlen = min(len(a),len(b))
    for i in range(minlen):
        if a[i] == b[i]:
            continue
        if X.index(a[i]) > X.index(b[i]):
            return True # a > b
        if X.index(a[i]) < X.index(b[i]):
            return False # b > a

    if len(a) > len(b):
        return True
    else:
        return False

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    # ここで分割を行う
    left = arr[:mid]
    right = arr[mid:]

    # 再帰的に分割を行う
    left = merge_sort(left)
    right = merge_sort(right)

    # returnが返ってきたら、結合を行い、結合したものを次に渡す
    return merge(left, right, X)


def merge(left, right, X):
    merged = []
    l_i, r_i = 0, 0

    # ソート済み配列をマージするため、それぞれ左から見ていくだけで良い
    while l_i < len(left) and r_i < len(right):
        # ここで=をつけることで安定性を保っている
        if hikaku(right[r_i],left[l_i], X):
            merged.append(left[l_i])
            l_i += 1
        else:
            merged.append(right[r_i])
            r_i += 1

    # 上のwhile文のどちらかがFalseになった場合終了するため、あまりをextendする
    if l_i < len(left):
        merged.extend(left[l_i:])
    if r_i < len(right):
        merged.extend(right[r_i:])
    return merged

S = merge_sort(S)

for i in range(N):
    print(*S[i],sep = '')
