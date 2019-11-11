from collections import deque
import sys
M, N, H = map(int, sys.stdin.readline().split())

field = {}

dx = (1, 0, 0, -1, 0 ,0)
dy = (0, 1, 0, 0, -1 ,0)
dz = (0, 0, 1, 0, 0 ,-1)

q = deque()

for i in range(H):
	field[i] = {}
	for j in range(N):
		field[i][j].append(list(map(int, sys.stdin.readline().split())))


for i in range(H):
	for j in range(N):
		for k in range(M):
			if field[i][j][k] == 1:
				q.append([k, j ,i])

while q:
	temp = q.popleft()
	for i in range(6):
		nx = temp[0] + dx[i]
		ny = temp[1] + dy[i]
		nz = temp[2] + dz[i]
		if nx < 0 or ny < 0 or nz < 0:
			continue
		if nx >= M  or ny >= N or nz >= H:
			continue
		if field[nz][ny][nx]:
			continue
		q.append([nx, ny, nz])
		check[nz][ny][nx] = check[temp[2]][temp[1]][temp[0]] + 1

ans = 0
for i in range(H):
	for j in range(N):
		if 0 in field[i][j]
				print(-1)
				sys.exit()
		ans = max(ans, max(field[i][j]))

print(ans - 1)


