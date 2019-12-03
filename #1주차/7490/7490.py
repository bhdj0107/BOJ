import sys
from collections import deque
N = int(sys.stdin.readline())
q = deque()
for _ in range(N):
    q.append(int(sys.stdin.readline()))

def dfs(D):
    global ans
    global temp
    if D%2 == 0:
        if ans[D] == temp:
            if cal() == 0:
                for i in range(temp*2-1):
                    print(ans[i],end='')
                print('\n',end='')
            return
        else:
            dfs(D + 1)
    else:
        ans[D] = ' '
        dfs(D + 1)
        ans[D] = '+'
        dfs(D + 1)
        ans[D] = '-'
        dfs(D + 1)

def cal():
    global ans
    global temp
    cq = deque()
    total = 0
    for i in range(temp*2-2,-1,-1):
        if ans[i] == '+':
            cnt = 0
            while cq:
                total += cq.popleft() * (10**cnt)
                cnt += 1
        elif ans[i] == '-':
            cnt = 0
            while cq:
                total -= cq.popleft() * (10**cnt)
                cnt += 1
        elif ans[i] == ' ':
            continue
        else:
            cq.append(ans[i])

    cnt = 0
    while cq:
        total += cq.popleft() * (10 ** cnt)
        cnt += 1

    return total

while q:
    ans = {}
    temp = q.popleft()
    for i in range(temp):
        ans[i*2] = i + 1
    dfs(0)
    print('\n',end='')