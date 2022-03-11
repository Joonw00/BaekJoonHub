import sys
N = input()
N = int(N)
p = input()
p = int(p)  #p쌍
pair = []
for _ in range(p):
    a,b = map(int, sys.stdin.readline().split())
    pair.append([a,b])
pair.sort()
#입력받고 정렬


vir = []
#모체 설정
vir.append(1)
n = 0

while len(vir)> n :
    for i in range(p):
        if vir[n] == pair[i][0] and pair[i][1] not in vir:
            vir.append(pair[i][1])
        #뒤의 컴퓨터가 바이러스, 앞의 것이 아직 걸린 적 없을 때
        elif vir[n] == pair[i][1] and pair[i][0] not in vir:
            vir.append(pair[i][0])
    n+=1

#에러 뜬 이유:2-1일 때, 2는 바이러스에 감염되는데, 고려 안함


#1제외
print(len(vir)-1)

