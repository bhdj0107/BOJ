import sys
N = int(sys.stdin.readline())
cnt = [0 for _ in range(N)]
temp = tuple(map(int, sys.stdin.readline().split()))
money = [0 for _ in range(N)]
M = int(sys.stdin.readline())
limit = int(M / N)

while sum(cnt) < N:
    for i in range(N):
        if temp[i] <= limit:
            money[i] = temp[i]
            cnt[i] = 1
    if sum(cnt) == N:
        print(max(money))
        exit()
    if limit == int((M - sum(money)) / (N - sum(cnt))):
        print(limit)
        exit()
    else:
        limit = int((M - sum(money)) / (N - sum(cnt)))

print(max(money))