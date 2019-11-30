import sys
X = int(sys.stdin.readline())
cnt = 0
total = 0
temp = 64
while temp:
    if total + temp > X:
        temp = int(temp / 2)
    else:
        total += temp
        temp = int(temp / 2)
        cnt += 1
print(cnt)