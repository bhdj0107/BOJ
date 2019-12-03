import sys

N, L, K = map(int, sys.stdin.readline().split())
sco = 0
easy = []


for i in range(N):
	if K == 0:
		break
	n1, n2 = map(int, sys.stdin.readline().split())
	if n2 > L:
		easy.append(n1)
		continue
	sco += 140
	K -= 1

for i in range(len(easy)):
	if K == 0:
		break
	if easy[i] <= L:
		sco += 100
		K -= 1

print(sco)