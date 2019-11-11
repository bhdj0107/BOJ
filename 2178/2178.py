from collections import deque

N, M = map(int, input().split())

q = deque()
dx = (1, 0, -1, 0)
dy = (0 ,1, 0, -1)
field = []
check = []
for i in range(N):
	temp = input()
	field.append([])
	check.append([])
	for j in range(M):
		field[i].append(int(temp[j]))
		check[i].append(0)

q.append([0,0])
check[0][0] = 1

while(1):
	try:
		temp = q.popleft()
		for i in range(4):
			nx = temp[0] + dx[i]
			ny = temp[1] + dy[i]
			if nx < 0 or ny < 0 or nx > M - 1 or ny > N - 1:
				continue
			if field[ny][nx] == 0 or check[ny][nx] != 0:
				continue
			q.append([nx, ny])
			check[ny][nx] = check[temp[1]][temp[0]] + 1
	except:
		break

print(check[N-1][M-1])