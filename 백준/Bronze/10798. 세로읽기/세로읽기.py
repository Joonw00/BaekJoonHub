import sys
word = []
for i in range(5):
    word.append(sys.stdin.readline().strip())
for i in range(15):
    for j in range(5):
        l = len(word[j]) # 현재 줄의 길이
        if l<=i:
            continue
        else:
            print(word[j][i], end='')