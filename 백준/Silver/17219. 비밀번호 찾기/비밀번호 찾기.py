import sys
N,M = map(int, sys.stdin.readline().split())
sav = {}
for i in range(N):
    ad, ps = sys.stdin.readline().split()
    sav[ad] = ps
for i in range(M):
    ad = sys.stdin.readline().rstrip()
    print("{0}".format(sav[ad]))
