import sys
sen_s = []
while 1:
    temp = sys.stdin.readline().rstrip()
    if temp == '*':
        break
    sen_s.append(temp)

for i in range(len(sen_s)):
    chk = False
    for D in range(1, len(sen_s[i])):
        temp = set()
        for index in range(len(sen_s[i]) - D):
            temp_2 = sen_s[i][index] + sen_s[i][index+D]
            if temp_2 in temp:
                chk = True
                break
            temp.add(temp_2)
        if chk:
            break
    if chk:
        print(sen_s[i] + " is NOT surprising.")
    else:
        print(sen_s[i] + " is surprising.")