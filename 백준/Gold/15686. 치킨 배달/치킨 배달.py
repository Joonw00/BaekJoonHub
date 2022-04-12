import sys
from itertools import combinations
N,M = input().split()
N = int(N)
M = int(M)
city = []
ch_ad = []
hm_ad = []
hn = 0
cn = 0 #초기 치킨집, 집 개수
for i in range(N):
  city.append(list(map(int,sys.stdin.readline().split())))
#치킨 집 주소 추가,집 주소 추가
for i in range(N):
  for j in range(N):
    if city[i][j] == 1:
      hn+=1
      hm_ad.append([j,i])
    elif city[i][j] == 2:
      ch_ad.append([j,i])
      cn+=1
ch_dist = [[0 for _ in range(hn)]for _ in range(cn)]

#치킨 거리 모두 계산
for i in range(cn):
  for j in range(hn):
    #i번째 치킨집과 j번째 집의 거리
    dx = abs(hm_ad[j][0]-ch_ad[i][0])
    dy = abs(hm_ad[j][1]-ch_ad[i][1])
    ch_dist[i][j] = dx+dy
#최종 계산
ans = []
for com_c in combinations(ch_dist,M):
  #print(com_c)
  ans_temp = 0
  for i in range(hn):
    m = 1000
    for j in range(M):
      if m > com_c[j][i]:
        m = com_c[j][i]
    ans_temp+=m
  ans.append(ans_temp)
print(min(ans))
