main_field = []
for _ in range(10):
	main_field.append(list(map(int, input().split())))
xy_field = [[[0,0] for _ in range(10)] for _ in range(10)]
cnt = 0
all_sum = 0

if (main_field[0][0] == 1):
	xy_field[0][0][0] = 1
	xy_field[0][0][1] = 1
for i in range(1, 10):
	if (main_field[0][i] == 1):
		xy_field[0][i][0] = xy_field[0][i-1][0] + 1
		xy_field[0][i][1] = 1
	if (main_field[i][0] == 1):
		xy_field[i][0][1] = xy_field[i-1][0][1] + 1
		xy_field[i][0][0] = 1
for i in range(1,10):
	for j in range(1,10):
		if (main_field[i][j] == 1):
			xy_field[i][j][0] = xy_field[i][j-1][0] + 1
			xy_field[i][j][1] = xy_field[i-1][j][1] + 1
for inv_size in range(5):
	size = 5 - inv_size
	size_cnt = 5
	for inv_i in range(10):
		i = 9 - inv_i
		if (size_cnt == 0):
			break
		for inv_j in range(10):
			temp = True
			j = 9 - inv_j
			if (size_cnt == 0):
				break
			if (main_field[i][j] == 1):
				for k in range(size):
					if (xy_field[i-k][j][0] < size):
						temp = False
				if(xy_field[i][j][0] >= size and xy_field[i][j][1] >= size and temp):
					cnt += 1
					size_cnt -= 1
					for k in range(size):
						for l in range(size):
							main_field[i-k][j-l] = 0



for i in range(10):
	all_sum += sum(main_field[i])
if (all_sum == 0):
	print(cnt)
else:
	print(-1)