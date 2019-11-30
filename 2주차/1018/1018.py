import sys
N, M = map(int, sys.stdin.readline().split())
field = {}
for i in range(N):
    field[i] = sys.stdin.readline().rstrip()

swap = {'W' : 'B' , 'B' : 'W'}
sample = {}
cnt = 0
temp = ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B']

def sampling(D):
    global temp
    global sample
    global cnt
    if D == 8:
        sample[''.join(temp)] = cnt
    else:
        sampling(D + 1)
        temp[D] = swap[temp[D]]
        cnt += 1
        sampling(D + 1)
        temp[D] = swap[temp[D]]
        cnt -= 1


sampling(0)

ans = 64
for i in range(N - 7):
    for j in range(M - 7):
        t1, t2 = 0, 0
        for k in (0, 2, 4 ,6):
            t1 += sample[field[i+k][j:j+8]]
            t2 += 8 - sample[field[i+k][j:j+8]]
        for k in (1, 3, 5 ,7):
            t2 += sample[field[i+k][j:j+8]]
            t1 += 8 - sample[field[i+k][j:j+8]]
        ans = min(ans, t1, t2)


print(ans)