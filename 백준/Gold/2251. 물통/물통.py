from collections import deque
import sys
ans = []
def FS(a,b,c):
    water = deque()
    water.append([a,b,c])
    while water:
        a,b,c = water.popleft()
        if visited[a][b][c] == True:
            continue
        visited[a][b][c] = True
        if a == 0:
            ans.append(c)
        if a>0: #A에서 이동
            if B != b: #다 안찼으면
                if b+a>=B:
                    water.append([a+b-B,B,c])
                else:
                    water.append([0,a+b,c])
            if C!=c:
                if c+a>=C:
                    water.append([a+c-C,b,C])
                else:
                    water.append([0,b,a+c])
        if b>0:
            if A!=a:
                if b+a>=A:
                    water.append([A,a+b-A,c])
                else:
                    water.append([a+b,0,c])
            if C!=c:
                if c+b>=C:
                    water.append([a,b+c-C,C])
                else:
                    water.append([a,0,b+c])
        if c>0:
            if A!=a:
                if a+c>=A:
                    water.append([A,b,a+c-A])
                else:
                    water.append([a+c,b,0])
            if B!=b:
                if b+c>=B:
                    water.append([a,B,b+c-B])
                else:
                    water.append([a,b+c,0])
A,B,C = map(int,sys.stdin.readline().split())
visited = [[[False for _ in range(C+1)]for _ in range(C+1)]for _ in range(C+1)]
FS(0,0,C)
ans.sort()

#주ㅡㅇ복제거,필요한가?
a = set(ans)
ans = list(a)
for i in range(len(ans)):
    print(ans[i],end=" ")