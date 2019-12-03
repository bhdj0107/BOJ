import sys
ans = 0
t_ans = 0
N = int(sys.stdin.readline())
A = tuple(map(int, sys.stdin.readline().split()))
mA = [0 for _ in range(N)]
count = [[] for _ in range(N)]
for i in range(N - 1, 0, -1):
    for j in range(i - 1, -1, -1):
        if A[i] > A[j]:
            count[i].append(j)

for i in range(N):
    temp = 0
    for j in count[i]:
        temp = max(temp, mA[j])
    mA[i] = temp + A[i]

print(max(mA))