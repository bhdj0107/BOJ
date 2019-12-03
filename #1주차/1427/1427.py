import sys

temp = sys.stdin.readline()

st = []
for i in range(len(temp)-1):
	st.append(int(temp[i]))

for i in range(len(st) - 1):
	for j in range(i + 1, len(st)):
		if st[i] < st[j]:
			st[i], st[j] = st[j], st[i]

for i in range(len(st)):
	print(st[i], end='')
