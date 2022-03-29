#풀이 방향 : 54321 = 50000 + 4000 + 300 + 20 + 1 를 이용
import sys
N = input()
N = int(N)
tot = [0 for _ in range(10)]
l = len(str(N))
n = str(N)
#십의 자리 부터
for i in range(1,l):
    i = int(i)
    num = int(n[l-i-1])
    temp = i*(10**(i-1))
    for j in range(1,10):
        j = int(j)
        tot[j]+=temp*num
    for j in range(1,num):
        j = int(j)
        tot[j]+=10**i
    tot[num]+=1

#일의 자리 처리
for i in range(1,(N%10) + 1):
    i = int(i)
    tot[i]+=1
#상위 자릿 수 불리는 횟수.높은 자리 부터
for i in range(l):
    tot[int(n[i])]+=N%(10**(l-1-i))

#0도 규칙 있는 거 같은데, 그냥 몸이 고생하는게 편할 듯
nonzero_sum = 0
tot_sum = sum(tot) - tot[0]

for i in range(l-1):
    nonzero_sum += (i+1) * 9 * (10**i)

if l != 1:
    nonzero_sum += (N - 10**(l-1) + 1) * l
    tot[0] = nonzero_sum - tot_sum
for i in range(10):
    print(tot[i], end=" ")