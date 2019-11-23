import sys
N = int(sys.stdin.readline())
cards = {}
temp = tuple(map(int, sys.stdin.readline().split()))
for i in temp:
    cards[i] = 1

N = int(sys.stdin.readline())
temp = tuple(map(int, sys.stdin.readline().split()))
for i in temp:
    try:
        print(cards[i], end=' ')
    except:
        print(0, end=' ')