import sys
N = int(sys.stdin.readline())
cnt = 0
while N:
	for i in range(1,N+1):
		if N < i:
			break
		N -= i
		cnt += 1
print(cnt)