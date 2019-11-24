import sys
M, N = map(int, sys.stdin.readline().split())
if M == N:
    print(2 * (M - 1))
else:
    if N > M:
        print(2 * (M - 1))
    else:
        print(2 * (N - 1) + 1)

