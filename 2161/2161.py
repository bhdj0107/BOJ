from collections import deque
q = deque()

N = int(input())

for i in range(1, N + 1):
	q.append(i)

while(1):
	try:
		print(q.popleft(), end='')
		print(" ", end='')
		q.append(q.popleft())
	except:
		break
