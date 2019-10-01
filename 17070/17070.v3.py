size = int(input())
field = []
for i in range(size):
	field.append(list(map(int, input().split())))
	field[i].append(1)

field.append([])
for i in range(size + 1):
	field[size].append(1)


field_check = [[[0,0,0] for _ in range(size)] for _ in range(size)]


field_check[0][1][0] = 1




for i in range(1, size):
	if (bool(field[0][i])):
		break
	field_check[0][i][0] += field_check[0][i-1][0]
for i in range(1, size):
	for j in range(1, size):
		if (bool(field[i][j])):
			continue
		field_check[i][j][0] += field_check[i][j-1][0] + field_check[i][j-1][1]
		field_check[i][j][2] += field_check[i-1][j][1] + field_check[i-1][j][2]
		if (bool(field[i][j-1]) or bool(field[i-1][j])):
			continue
		field_check[i][j][1] += sum(field_check[i-1][j-1])

			
print(sum(field_check[size-1][size-1])) 