import sys

N = int(sys.stdin.readline())
ls = {}

for _ in range(N):
	ls[int(sys.stdin.readline())] = 1

for i in range(-1000000,1000001):
	try:
		a = ls[i]
		print(i)
	except:
		continue

