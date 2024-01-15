import sys
s = sys.stdin.readline().strip()
l = len(s)
temp = [] #flag 0이면 뒤집어서 넣기
flag = 0 #0이면 <>안에 있지 않음, 1이면 <>안에 있음
for i in range(l):
    if s[i] == '<':
        while temp:
            print(temp.pop(), end='')
        flag = 1
    elif s[i] == '>':
        print(s[i], end='')
        flag = 0
        continue
    if flag == 1:
        print(s[i], end='')
        continue
    elif flag == 0:
        if s[i] != ' ':
            temp.append(s[i])
        else:
            while temp:
                print(temp.pop(), end='')
            print(' ', end='')

while temp:
    print(temp.pop(), end='')
    