# N = int(input())
# field = {}
# c_field = []
# cst = 0
# check = [[False for _ in range(N-2)] for _ in range(N-2)]
# dx = (1,0,-1,0,0,2,1,1,0,0,-1,-1,-2)
# dy = (0,1,0,-1,0,0,1,-1,2,-2,1,-1,0)
# for i in range(N):
# 	field[i] = list(map(int, input().split()))

# for i in range(1, N-1):
# 	c_field.append([])
# 	for j in range(1, N-1):
# 		temp = field[i][j]
# 		for k in range(4):
# 			nx = j + dx[k]
# 			ny = i + dy[k]
# 			temp += field[ny][nx]
# 		c_field[i-1].append(temp)
# c_field.append([201])


a = [[1], [2]]
if 1 in a:
	print(True)
