import sys

doc = sys.stdin.readline()
seq = sys.stdin.readline()
seq = seq[0:len(seq)-1]
cnt = 0
i = 0
while i < len(doc) - 1:
	if doc[i:i+len(seq)] == seq:
		i += len(seq)
		cnt += 1
	i += 1
print(cnt)
