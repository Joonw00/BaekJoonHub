import sys
n = int(input())


cost = list(map(int,sys.stdin.readline().split()))
cost.sort()

m = int(input())

def sumMid(mid):
    sum = 0
    for i in range(n):
        if mid >= cost[i]:
            sum+=cost[i]
        else:
            sum+=mid
    return sum

start = 0
end = cost[-1]

while start <= end:
    mid = (start+end) // 2
    sum = sumMid(mid)
    if sum <= m:
        start= mid + 1
    else:
        end = mid- 1

print(end)