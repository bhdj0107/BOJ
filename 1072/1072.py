import sys
X, Y = map(int, sys.stdin.readline().split())
Z = int(Y/X*100 + 1)

temp = 0
if Z >= 100:
    print(-1)
else:
    for digit in range(10):
        for _ in range(10):
            temp += (10 ** (9 - digit))
            if int((Y+temp) / (X+temp) * 100) >= Z:
                break
        temp -= (10 ** (9 - digit))

print(temp + 1)