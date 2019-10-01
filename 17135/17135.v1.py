N, M, D = map(int, input().split())
field = []
wave_end = []
for i in range(N):
	field.append(list(map(int, input().split())))

for x in range(M):
	wave_end.append(field)
	for inv_y in range(N):
		y = N - inv_y - 1
		check = 0
		for dist in range(D):
			pointer_x = x - dist
			pointer_y = y
			for i in range(dist+dist+1):
				if (wave_end[x][pointer_y][pointer_x] == 1):
					wave_end[x][pointer_y][pointer_x] = 0
					check = 1
					break
				if (i < dist and dist != 0):
					pointer_x += 1
					pointer_y += 1
				elif (i >= dist and dist != 0):
					pointer_x -= 1
					pointer_y -= 1
			if (check == 1):
				break
for i in range(M):
	for j in range(N):
		print(wave_end[i][j])
	print("\n\n")







