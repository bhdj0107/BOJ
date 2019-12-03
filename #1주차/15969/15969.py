import sys
sys.stdin.readline()
S = tuple(map(int, sys.stdin.readline().split()))
print(max(S)-min(S))