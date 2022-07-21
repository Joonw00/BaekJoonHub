import sys
n = int(input())
dic = []
for i in range(n):
    dic.append(list(sys.stdin.readline().split()))
dic.sort(key=lambda x: x[0])
dic.sort(key=lambda x: int(x[3]), reverse=True)
dic.sort(key=lambda x: int(x[2]))
dic.sort(key=lambda x: int(x[1]), reverse=True)
for i in dic:
    print(i[0])