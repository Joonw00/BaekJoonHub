import sys
n,m = map(int,sys.stdin.readline().split())



basket = [i for i in range(n+1)]
for i in range(m):
    i, j = map(int,sys.stdin.readline().split())
    temp = basket[i]
    basket[i] = basket[j]
    basket[j] = temp

for i in range(1, n+1):
    print(basket[i], end=" ")