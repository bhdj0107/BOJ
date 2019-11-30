in_out = [0]
for i in range(1, 5):
    a, b = map(int, input().split())
    temp = in_out[i - 1] + b - a
    if temp < 0:
        temp = 0
    if temp > 10000:
        temp = 10000
    in_out.append(temp)

print(max(in_out))


