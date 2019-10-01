size = int(input())
field = []
for i in range(size):
	field.append(list(map(int, input().split())))
	field[i].append(1)

field.append([])
for i in range(size + 1):
	field[size].append(1)

field_check = []
for i in range(size+1):
	field_check.append([])
	for j in range(size+1):
		field_check[i].append(0)

def find_route_x(x, y, check):
	if (not bool(check)):
		find_route_x(x + 1, y, (field[y][x+1] + 4 * field[y+1][x+1] + 6 * field[y+1][x]) % 2)
		find_route_xy(x + 1, y + 1, field[y][x+1] + field[y+1][x+1] + field[y+1][x])
	
	field_check[y][x] += 1

def find_route_y(x, y, check):
	if (not bool(check)):
		find_route_y(x, y + 1, (field[y][x+1] + 4 * field[y+1][x+1] + 6 * field[y+1][x]) // 6)
		find_route_xy(x + 1, y + 1, field[y][x+1] + field[y+1][x+1] + field[y+1][x])

	field_check[y][x] += 1

def find_route_xy(x, y, check):
	count = 0
	if (not bool(check)):
		find_route_x(x + 1, y, (field[y][x+1] + 4 * field[y+1][x+1] + 6 * field[y+1][x]) % 2)
		find_route_xy(x + 1, y + 1, field[y][x+1] + field[y+1][x+1] + field[y+1][x])
		find_route_y(x, y + 1, (field[y][x+1] + 4 * field[y+1][x+1] + 6 * field[y+1][x]) // 6)

	field_check[y][x] += 1
x = 1
y = 0
find_route_x(x, y, (field[y][x+1] + 4 * field[y+1][x+1] + 6 * field[y+1][x]) % 2)
print(field_check[size-1][size-1])