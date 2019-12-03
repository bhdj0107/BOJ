# heapq 모듈 사용, 시간 비교 하려구 ㅋㅋ

import heapq
import sys
heap = []
N = int(sys.stdin.readline())
comm = {}
for i in range(N):
    comm[i] = int(sys.stdin.readline())

for i in range(N):
    if comm[i] == 0:
        if len(heap) == 0:
            print(0)
        else:
            print(heapq.heappop(heap))
    else:
        heapq.heappush(heap, comm[i])