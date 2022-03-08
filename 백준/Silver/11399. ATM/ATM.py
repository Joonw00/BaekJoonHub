import sys
N = input()
N = int(N)
P = list(map(int, sys.stdin.readline().split()))

P.sort()
sum = 0
tot = []
for i in range(N):
    sum += P[i]
    tot.append(sum)
ans = 0
for i in range(len(tot)):
    ans+=tot[i]

print(ans)