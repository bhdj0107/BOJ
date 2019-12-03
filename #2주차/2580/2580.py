import sys
sys.setrecursionlimit(10**6)
x, y = 0, 0
nums = {1,2,3,4,5,6,7,8,9}
field = {}
pos = {}
cnt = 0
for i in range(9):
    for j in range(9):
        pos[cnt] = tuple([i, j])
        cnt += 1

for i in range(9):
    field[i] = list(map(int, sys.stdin.readline().split()))


def no_nums_hor(index):
    global nums
    return nums - set(field[index])


def no_nums_vert(index):
    global nums
    temp = set()
    for i in range(9):
        temp.add(field[i][index])

    return nums - temp


def no_nums_sect(x_index, y_index):
    temp = set()
    x_index = int(x_index / 3)
    y_index = int(y_index / 3)

    for i in range(3):
        temp = temp.union(field[y_index * 3 + i][x_index * 3:x_index * 3 + 3])

    return nums - temp


def dfs(D):
    global field
    if D == 81:
        for i in range(9):
            for j in range(9):
                print(field[i][j], end=' ')
            print('\n', end='')
        exit()
    else:
        x, y = pos[D][0], pos[D][1]
        if field[y][x] == 0:
            for num in no_nums_sect(x, y) & no_nums_vert(x) & no_nums_hor(y):
                field[y][x] = num
                dfs(D + 1)
                field[y][x] = 0
        else:
            dfs(D + 1)

dfs(0)