import sys
X, Y = map(int, sys.stdin.readline().split())
Z = Y * 100 // X

Max = 1000000000
Min = 0

if Z >= 99:
    print(-1)
    exit()
else:
    while Min <= Max:
        Mid = (Max + Min) // 2
        temp = (Y+Mid) * 100 // (X+Mid)
        if temp > Z:
            Max = int(Mid) - 1
            continue
        else:
            Min = int(Mid) + 1

print(Min)