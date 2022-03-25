#A~J가 아니었어???
import sys
N = input()
N = int(N)
#A~J 를 8자리
Alpha = [[0 for _ in range(26)]for _ in range(8)]
for i in range(N):
    a = sys.stdin.readline().split()
    j = 0
    for i in range(len(a[0])-1,-1,-1):
        i = int(i)
        al = ord(a[0][i]) - 65
        Alpha[j][al]+=1
        j+=1
#카운트
al_count = [0] * 26
for i in range(26):
    for j in range(8):
        al_count[i]+=Alpha[j][i] * (10**j)
al_count.sort(reverse=True)
ans = 0
#역순으로 바꿔야 할 듯
j = 9
for i in range(26):
    ans+= j*al_count[i]
    j-=1

print(ans)
