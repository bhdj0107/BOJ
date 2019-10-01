size = int(input())
field = []
for i in range(size):
	field.append(input().split())
	for j in range(size):
		field[i][j] =  int(field[i][j])
	field[i].append(1)

field.append([])
for i in range(size + 1):
	field[size].append(1)

def find_route(size, field, x, y, d):
	count = 0
	if (d == 0):
		if (not bool(field[y][x+1])):
			count += find_route(size, field, x + 1, y, 0)
		if (not (bool(field[y][x+1]) or bool(field[y+1][x]) or bool(field[y+1][x+1]))):
			count += find_route(size, field, x + 1, y + 1, 1)

	if (d == 1):
		if (not bool(field[y][x+1])):
			count += find_route(size, field, x + 1, y, 0)
		if (not (bool(field[y][x+1]) or bool(field[y+1][x]) or bool(field[y+1][x+1]))):
			count += find_route(size, field, x + 1, y + 1, 1)
		if (not bool(field[y+1][x])):
			count += find_route(size, field, x, y + 1, 2)

	if (d == 2):
		if (not (bool(field[y][x+1]) or bool(field[y+1][x]) or bool(field[y+1][x+1]))):
			count += find_route(size, field, x + 1, y + 1, 1)
		if (not bool(field[y+1][x])):
			count += find_route(size, field, x, y + 1, 2)

	if (x == y and x == size - 1):
		return 1
	else:
		return count

print(find_route(size,field,1,0,0))
