import sys
a,b = map(int,sys.stdin.readline().split())
A = []
A.append([a,1])
while True:
    if len(A) == 0:
        print(-1)
        break
    temp = A.pop()
    if temp[0] == b:
        print(temp[1])
        break
    if temp[0] * 2 == b or temp[0] * 10 + 1 == b:
        print(temp[1]+1)
        break
    if temp[0] * 2 < b:
        A.append([temp[0]*2,temp[1]+1])
    if temp[0] * 10 + 1 < b:
        A.append([temp[0]*10+1,temp[1]+1])
