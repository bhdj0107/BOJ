import sys
K = int(sys.stdin.readline()) + 8
aa = {}
for i in range(8):
    aa[i] = i + 1
N = int(sys.stdin.readline())
t = 210

while t > 0:
    a, b = sys.stdin.readline().split()
    if b == 'T':
        K += 1
    t -= int(a)

if b == 'T':
    print(aa[(K - 2) % 8])
else:
    print(aa[(K - 1) % 8])
