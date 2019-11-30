import sys
N, K = map(int, sys.stdin.readline().split())
ls = list(map(int, sys.stdin.readline().split()))
ls.sort()

print(ls[K-1])