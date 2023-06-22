import sys
n, k = map(int, sys.stdin.readline().split())
coin = []
for i in range(n):
    coin.append(int(sys.stdin.readline()))

total = [0 for i in range(k+1)]
total[0] = 1

for i in coin:
    for j in range(i, k+1):
        total[j] += total[j-i]
        
print(total[k])