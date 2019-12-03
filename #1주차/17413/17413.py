import sys
from collections import deque

temp = sys.stdin.readline()
tq = False
q = deque()
for i in range(len(temp) - 1):
    if tq:
        if temp[i] == '>':
            tq = False
        print(temp[i], end='')
    else:
        if temp[i] == ' ':
            while q:
                print(q.pop(), end='')
            print(' ', end='')
        elif temp[i] == '<':
            while q:
                print(q.pop(), end='')
            print('<', end='')
            tq = True
            continue
        else:
            q.append(temp[i])
while q:
    print(q.pop(), end='')