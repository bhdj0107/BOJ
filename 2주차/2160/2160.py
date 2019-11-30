import sys
N = int(sys.stdin.readline())
ans = (0, 0, 36)
pic = {}
pic_set = [set() for _ in range(N)]
for i in range(N):
    temp = []
    for _ in range(5):
        temp.append(sys.stdin.readline().rstrip())
    pic[i] = temp

for i in range(N):
    for y in range(5):
        for x in range(7):
            if pic[i][y][x] == 'X':
                pic_set[i].add((x, y))

for i in range(N - 1):
    for j in range(i + 1, N):
        temp = len((pic_set[i] | pic_set[j]) - (pic_set[i] & pic_set[j]))
        if temp < ans[2]:
            ans = (i, j, temp)

print(ans[0] + 1, ans[1] + 1)

