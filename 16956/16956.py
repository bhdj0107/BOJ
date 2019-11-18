import sys
dx = (1,0,-1,0)
dy =(0,1,0,-1)
R, C = map(int, sys.stdin.readline().split())
field = {}
for i in range(R):
	field[i] = sys.stdin.readline()[0:C]

for i in range(R):
	for j in range(C):
		if field[i][j] == 'W':
			for k in range(4):
				nx = j + dx[k]
				ny = i + dy[k]
				if nx < 0 or ny < 0 or nx >= C or ny >= R:
					continue
				if field[ny][nx] == '.':
					field[ny] = field[ny][0:nx] + 'D' + field[ny][nx+1:C]
				if field[ny][nx] == 'S':
					print(0)
					exit()
print(1)
for i in range(R):
	print(field[i])
