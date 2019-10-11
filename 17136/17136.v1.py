import copy

main_field = [list(map(int, input().split())) for _ in range(10)]
size_cnt = [5, 5, 5, 5, 5]
cnt = -1
total_cnt = 0
for i in range(10):
    total_cnt += sum(main_field[i])

def check_paper(size, x, y, field):
    temp = 0
    if x + size - 1 >= 10:
        return False
    for i in range(size):
        temp += sum(field[y + i][x:x + size])
    if temp == size * size:
        return True
    return False


def dfs(px, py, previous_field, depth, total_cnt):
    global cnt
    if cnt != -1 and depth > cnt:
        return
    if py == 10 or total_cnt == 0:
        if cnt == -1 or depth < cnt:
            cnt = depth
        return

    if previous_field[py][px] == 1:
        temp_field = copy.deepcopy(previous_field)
        for size in range(1, 6):
            if size_cnt[size - 1] == 0:
                continue
            if check_paper(size, px, py, temp_field):
                total_cnt -= 1
                size_cnt[size - 1] -= 1
                for x in range(size):
                    for y in range(size):
                        temp_field[py+y][px+x] = 0
            if px != 9:
                dfs(px + 1, py, temp_field, depth + 1, total_cnt)
            else:
                dfs(0, py + 1, temp_field, depth + 1, total_cnt)
    else:
        if px != 9:
            dfs(px + 1, py, previous_field, depth, total_cnt)
        else:
            dfs(0, py + 1, previous_field, depth, total_cnt)


dfs(0, 0, main_field, 0, total_cnt)
print(cnt)
