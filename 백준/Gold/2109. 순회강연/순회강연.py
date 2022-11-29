from queue import PriorityQueue
import sys
n = int(input())
q = PriorityQueue()
for i in range(n):
    p,d = map(int,sys.stdin.readline().split())
    q.put([-p,d])
lec = [0]*10001
while not q.empty():
    p,d = q.get()
    p = -p
    for i in range(d,0,-1):
        if lec[i] == 0:
            lec[i] = p
            break
print(sum(lec))