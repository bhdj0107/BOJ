import sys
N = int(sys.stdin.readline())
document = []
for _ in range(N):
    document.append(sys.stdin.readline().rstrip())

for i in range(N):
    temp = "".join(tuple(reversed(list(document[i]))))
    if temp in document:
        print(len(document[i]), end=' ')
        print(document[i][int(len(document[i]) / 2)])
        exit()