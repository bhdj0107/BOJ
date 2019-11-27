import sys

N, M, L = map(int, sys.stdin.readline().split())
index = 0
b_cnt = [0 for _ in range(N)]
direction = {0: -L, 1: L}
cnt = 0
while 1:
    if index < 0:
        index += N
    else:
        index = index % N
    b_cnt[index] += 1
    if b_cnt[index] == M:
        print(cnt)
        exit()
    else:
        index += direction[b_cnt[index] % 2]
    cnt += 1
