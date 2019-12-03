import sys
N = int(sys.stdin.readline())
ans = 0
board = []
CYPZ = ('C', 'Y', 'P', 'Z')
for _ in range(N):
    board.append(list(sys.stdin.readline().rstrip()))

for y in range(N):
    for x in range(N):

        # 가로축 교환
        if x < N - 1:
            board[y][x], board[y][x+1] = board[y][x+1], board[y][x]
            t1_line = "".join(board[y])
            t2_line = "".join(tuple(zip(*board))[x])
            t3_line = "".join(tuple(zip(*board))[x+1])
            board[y][x], board[y][x+1] = board[y][x+1], board[y][x]

            for i in range(2, N+1):
                if ans > i:
                    continue
                for j in range(4):
                    check = "".join([CYPZ[j] for _ in range(i)])
                    if check in t1_line or check in t2_line or check in t3_line:
                        ans = i

        # 세로축 교환
        if y < N - 1:
            board[y+1][x], board[y][x] = board[y][x], board[y+1][x]
            t1_line = "".join(board[y])
            t2_line = "".join(board[y+1])
            t3_line = "".join(tuple(zip(*board))[x])
            board[y+1][x], board[y][x] = board[y][x], board[y+1][x]

            for i in range(2, N+1):
                if ans > i:
                    continue
                for j in range(4):
                    check = "".join([CYPZ[j] for _ in range(i)])
                    if check in t1_line or check in t2_line or check in t3_line:
                        ans = i

print(ans)