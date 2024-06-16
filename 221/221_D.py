from collections import Counter


def main():
    N = int(input())
    C = Counter()
    for _ in range(N):
        a, b = map(int, input().split())
        C[a] += 1  # a日目に1人増えます
        C[a + b] -= 1  # a + b 日目に1人減ります
    
    #print(C)

    ans = [0] * (N + 1)  # ans[i]: ちょうどi人がログインしていた日数
    days = sorted(C.keys())  # 人数が変化する日のリストを昇順
    prev_day = 0  # 前回人数が変化した日
    cnt = 0  # ログインしている人数
    for curr_day in days:
        ans[cnt] += curr_day - prev_day
        cnt += C[curr_day]
        prev_day = curr_day

    print(*ans[1:])  # 0人の日は出力しません


if __name__ == '__main__':
    main()