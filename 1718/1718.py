import sys
sen = sys.stdin.readline().rstrip()
key = sys.stdin.readline().rstrip()

pair = {}
for i in range(26):
    pair[i+97] = chr(i+97)
    pair[chr(i+97)] = i+97
for i in range(len(sen)):
    if sen[i] == ' ':
        print(' ', end='')
    else:
        print(pair[97 + abs(25 + pair[sen[i]] - pair[key[i % len(key)]]) % 26], end='')