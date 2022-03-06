import sys
C, N = map(int, sys.stdin.readline().split())   #N개도시에서 C명 확보
cost = []
cust = []

for _ in range(N):
    a,b = map(int, sys.stdin.readline().split())
    cost.append(a)
    cust.append(b)

total = [0]*(C+100)       #인덱스에 해당하는 최소 도달 비용 입력

for n in range(C+100):    #n은 계산된 인덱스
    for i in range(N):  #i는 cost,cust가 호출될 인덱스
        if n+cust[i] < C+100:  #배열 범위 내에서
            if total[n] == 0 and n!=0:   #현재 인덱스에 아무 값도 들어있지 않으면 패스
                continue
            if total[n+cust[i]] == 0 or total[n+cust[i]] > total[n]+cost[i]:
                total[n+cust[i]] = total[n] + cost[i]

ans = total[C]
if ans == 0:
    ans = 1e9
for i in range(100):
    if ans > total[i+C] and total[i+C] != 0:
        ans = total[i+C]

print(ans)