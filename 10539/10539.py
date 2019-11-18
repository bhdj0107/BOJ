import sys
from collections import deque

q = deque()
N = int(sys.stdin.readline())
B = tuple(map(int, sys.stdin.readline().split()))

for i in range(1 ,N+1):
	q.append(B[i-1]*i-sum(q))
	print(q[i-1], end=' ')


