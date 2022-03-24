import sys
from collections import deque
N = input()
N = int(N)
K = input()
K = int(K)

ap = []
for i in range(K):
    b,a = map(int, sys.stdin.readline().split())
    ap.append([a,b])
L = input()
L = int(L)

turn = []
for i in range(L):
    a,b = sys.stdin.readline().split()
    a = int(a)
    turn.append([a,b])

turn_idx = 0
#지나간 좌표를 모두 저장, ap가 포함된 횟수만큼 정답 추가
t = 0 #지난 시간

rt = deque()
x = 1
y = 1
rt.append([x,y])
drt = 0 #0:우,1:하,2:좌,3:상
eat = []
while True:
    t+=1
    if drt == 0:
        x+=1
        if [x,y] in rt:
            break
        rt.append([x,y])
    elif drt == 1:
        y+=1
        if [x,y] in rt:
            break
        rt.append([x,y])
    elif drt == 2:
        x-=1
        if [x,y] in rt:
            break
        rt.append([x,y])
    elif drt == 3:
        y-=1
        if [x,y] in rt:
            break
        rt.append([x,y])
    
    if [x,y] in ap and [x,y] not in eat:
        eat.append([x,y])
    else:
        rt.popleft()
        

    if turn_idx <L:
        if turn[turn_idx][0] == t:
            if turn[turn_idx][1] == 'D':
                drt=(drt+1)%4
            elif turn[turn_idx][1] == 'L':
                drt=(drt+3)%4
            turn_idx+=1
    if 1>x or x>N or 1>y or y>N:
        break

print(t)