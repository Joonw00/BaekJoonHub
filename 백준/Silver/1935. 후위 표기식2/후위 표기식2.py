import sys
n = int(sys.stdin.readline())
cal = input()
l = len(cal)
s = []
alp = []
for i in range(n):
    alp.append(int(sys.stdin.readline()))
for i in range(l):
    if 'A' <= cal[i] <= 'Z':
        temp = (ord(cal[i]) - ord('A'))
        s.append(alp[temp])
    elif cal[i] == '+':
        temp = s.pop()
        temp += s.pop()
        s.append(temp)
    elif cal[i] == '-':
        temp = s.pop()
        temp -= s.pop()
        s.append(-temp)
    elif cal[i] == '*':
        temp = s.pop()
        temp *= s.pop()
        s.append(temp)
    elif cal[i] == '/':
        a = s.pop()
        b = s.pop()
        temp = b / a
        s.append(temp)
ans = s.pop()
print('%.2f' % ans)
