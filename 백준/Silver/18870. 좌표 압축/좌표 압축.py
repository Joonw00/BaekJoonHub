import sys
n = input()
n =int(n)
X = list(map(int, sys.stdin.readline().split()))
comp = list(set(X))
comp.sort()
dic = {comp[i]:i for i in range(len(comp))}
for i in X:
    print(dic[i], end=' ')    