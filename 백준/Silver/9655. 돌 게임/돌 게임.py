import sys
n = int(sys.stdin.readline())

win = [0] * 1001

# 1이면 상근이가 이김, 0이면 창영이가 이김
win[1] = 1
win[2] = 0
win[3] = 1

for i in range(4, 1001):
    if win[i-1] == 0 or win[i-3] == 0:
        win[i] = 1
    else:
        win[i] = 0


if win[n] == 1:
    print("SK")
else:
    print("CY")