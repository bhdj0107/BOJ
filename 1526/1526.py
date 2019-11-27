import sys
N = int(sys.stdin.readline().rstrip())
ans = 0

def dfs(D, s):
    global ans
    if int(s) <= N:
        ans = max(ans ,int(s))
    if D == 7:
        return
    else:
        for n in '47':
            dfs(D+1,s+n)

dfs(0, '0')
print(ans)

