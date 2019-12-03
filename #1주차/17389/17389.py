import sys
from collections import deque
q = deque()
ans = 0
N = int(sys.stdin.readline())
S = sys.stdin.readline()[0:N] + "X"
def ssum(n1, n2):
	global ans
	for i in range(n1, n2+1):
		ans += i
if S[0] == 'O':
	q.append(0)
for i in range(1,N+1):
	if S[i] == S[i-1]:
		continue
	if S[i] == 'X':
		temp = q.pop()
		ssum(temp+1, i)
		ssum(0, i-temp-1)
	if S[i] == 'O':
		q.append(i)
print(ans)