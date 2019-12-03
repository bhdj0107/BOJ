import sys
sys.setrecursionlimit(10**8)
S = sys.stdin.readline().rstrip()
N = int(sys.stdin.readline())
len_S = len(S)
cnt = 0
words = {}
words_l = {}


count = [[] for _ in range(len_S)]

for i in range(N):
    words[i] = sys.stdin.readline().rstrip()
    words_l[i] = len(words[i])

for i in range(len_S):
    for j in range(N):
        if S[i:i+words_l[j]] == words[j]:
            count[i].append(words_l[j])

def find_route(D):
    if D == len_S:
        print(1)
        exit()
    elif D < len_S:
        for i in count[D]:
            find_route(D + i)

find_route(0)
print(0)