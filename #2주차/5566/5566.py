import sys

N, M = map(int, sys.stdin.readline().split())
board = {}
dice = {}
index = 0
for i in range(N):
    board[i] = int(sys.stdin.readline())

for i in range(M):
    dice[i] = int(sys.stdin.readline())

for i in range(M+1):
    if index >= N - 1:
        print(i)
        break
    if index + dice[i] >= N - 1:
        print(i+1)
        break
    index += dice[i] + board[index + dice[i]]