import sys
N, M = map(int, sys.stdin.readline().split())
g = {}
n = {}
p = {}
for i in range(N):
	g[i] = input()
	temp = []
	t = int(input())
	for j in range(t):
		temp.append(input())
	temp.sort()
	n[i] = temp

for i in range(M):
	temp = []
	temp.append(input())
	temp.append(input())
	p[i] = temp

for i in range(M):
	if p[i][1] == '1':
		for j in range(N):
			if p[i][0] in n[j]:
				print(g[j])
				break
	else:
		for j in range(N):
			if p[i][0] == g[j]:
				for k in n[j]:
					print(k)
				break

