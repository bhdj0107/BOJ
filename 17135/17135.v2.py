import copy
N, M, D = map(int, input().split())
field = []
global wave_end
result = []
maxi = 999999999
s_total = 0

for i in range(N):
	field.append(list(map(int, input().split())))
for i in range(N):
	result.append(list(map(int, field[i])))
for i in range(N):
	s_total += sum(field[i])
for x1 in range(M-2):
	for x2 in range(x1 + 1,M-1):
		for x3 in range(x2 + 1, M):
			wave_end = []
			for i in range(3):
				wave_end.append(copy.deepcopy(field))
			for inv_y in range(N):
				y = N - inv_y - 1
				def wave(xpos, apos):
					check = 0
					for dist in range(D):
						pointer_x = xpos - dist
						pointer_y = y
						for i in range(dist+dist+1):
							if (pointer_x < 0):
								pointer_x += 1
								pointer_y -= 1
								continue
							if (pointer_x >= M):
								continue
							if (pointer_y >= 0 and wave_end[apos][pointer_y][pointer_x] == 1):
								wave_end[apos][pointer_y][pointer_x] = 0
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
				wave(x1, 0)
				wave(x2, 1)
				wave(x3, 2)
				for i in range(N):
					for j in range(M):
						result[i][j] = wave_end[0][i][j] * wave_end[1][i][j] * wave_end[2][i][j]
				wave_end[0] = copy.deepcopy(result)
				wave_end[1] = copy.deepcopy(result)
				wave_end[2] = copy.deepcopy(result)
			total = 0
			for l in range(N):
				total += sum(result[l])
			if (total < maxi):
				maxi = total

print(s_total - maxi)