import sys

N, M = map(int, sys.stdin.readline().split())
y = set()
x = set()
castle = []
for _ in range(N):
	castle.append(sys.stdin.readline()[0:M])

for i in range(N):
	for j in range(M):
		if castle[i][j] == 'X':
			x.add(j)
			y.add(i)
			
print(max(M-len(x),N-len(y)))