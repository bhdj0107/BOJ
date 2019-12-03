import sys
X1 = sys.stdin.readline().rstrip()
X2 = sys.stdin.readline().rstrip()
ans = 0
X1_dict = {chr(i):0 for i in range(97, 123)}
X2_dict = {chr(i):0 for i in range(97, 123)}
for i in range(len(X1)):
    X1_dict[X1[i]] += 1
for i in range(len(X2)):
    X2_dict[X2[i]] += 1

for i in range(97, 123):
    ans += abs(X1_dict[chr(i)] - X2_dict[chr(i)])

print(ans)