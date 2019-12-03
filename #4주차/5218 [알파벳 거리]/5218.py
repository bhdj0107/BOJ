import sys
N = int(sys.stdin.readline())
for i in range(N):
    temp_1, temp_2 = sys.stdin.readline().split()
    print("Distances:", end=' ')
    for j in range(len(temp_1)):
        print((26 + (ord(temp_2[j]) - ord((temp_1[j])))) % 26, end=' ')
    print('\n', end='')
