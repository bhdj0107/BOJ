import sys
L = int(sys.stdin.readline())
A = int(sys.stdin.readline())
B = int(sys.stdin.readline())
C = int(sys.stdin.readline())
D = int(sys.stdin.readline())

temp = max(A / C, B / D)
if temp == int(temp):
    print(L - int(temp))
else:
    print(L - int(temp) - 1)