import sys
N, L, D = map(int, sys.stdin.readline().split())

end = L * N + 5 * (N - 1)

i = D
while i < end:
    if i % (L + 5) - L >= 0:
        print(i)
        exit()
    else:
        i += D

print(i)