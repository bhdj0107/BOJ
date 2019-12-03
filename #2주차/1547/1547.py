N = int(input())
ball = [True, False, False]
for _ in range(N):
    a, b = map(int, input().split())
    ball[a - 1], ball[b - 1] = ball[b - 1], ball[a - 1]

for i in range(3):
    if ball[i]:
        print(i + 1)