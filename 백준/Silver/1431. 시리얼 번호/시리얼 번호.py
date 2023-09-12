import sys
n = int(sys.stdin.readline())

def sumNum(x):
    sumline = 0
    for i in range(len(x)):
        if x[i].isdigit():
            sumline += int(x[i])
    return sumline

ser = []
for i in range(n):
    ser.append(sys.stdin.readline().rstrip())

ser.sort(key = lambda x: (len(x), sumNum(x),x))
for i in range(n):
    print(ser[i])