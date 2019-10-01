N, M, D = map(int, input().split())
field = []
wave_end = []
result = []
maxi = 999999999
s_total = 0

for i in range(N):
	field.append(list(map(int, input().split())))
for i in range(N):
	result.append(list(map(int, field[i])))
for i in range(N):
	s_total += sum(field[i])
for x in range(M):
	wave_end.append([])
	for i in range(N):
		wave_end[x].append(list(map(int, field[i])))
	for inv_y in range(N):
		y = N - inv_y - 1
		check = 0
		for dist in range(D):
			pointer_x = x - dist
			pointer_y = y
			for i in range(dist+dist+1):
				if (pointer_x < 0):
					pointer_x += 1
					pointer_y -= 1
					continue
				if (pointer_x >= M):
					continue
				if (wave_end[x][pointer_y][pointer_x] == 1):
					wave_end[x][pointer_y][pointer_x] = 0
					check = 1
					break
				if (i < dist and dist != 0):
					pointer_x += 1
					pointer_y -= 1
				elif (i >= dist and dist != 0):
					pointer_x += 1
					pointer_y += 1
			if (check == 1):
				break

for i in range(M-2):
	for j in range(i+1,M-1):
		for k in range(i+2,M):					
			for x in range(M):
				for y in range(N):
					result[y][x] = wave_end[i][y][x] * wave_end[j][y][x] * wave_end[k][y][x]
			total = 0
			for l in range(N):
				total += sum(result[l])
			if (total < maxi):
				maxi = total

print(s_total - maxi)