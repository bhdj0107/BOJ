import sys

N = int(sys.stdin.readline())
temp = tuple(map(int, sys.stdin.readline().split()))
ls = {}
for i in temp:
	ls[i] = 1

N = int(sys.stdin.readline())
temp = tuple(map(int, sys.stdin.readline().split()))
for i in temp:
	try:
		a = ls[i]
		print(1)
	except:
		print(0)

