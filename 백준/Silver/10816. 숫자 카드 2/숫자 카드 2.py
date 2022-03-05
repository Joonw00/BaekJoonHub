from bisect import bisect_left, bisect_right
from sys import stdin
import sys
sys.setrecursionlimit(10**7)
global count
N = input()
N = int(N)
cards = list(map(int, sys.stdin.readline().split()))     #상근이가 갖고 있는 카드
len_whole = int(len(cards))      #전체 길이
M = input()
M = int(M)
nums = list(map(int, sys.stdin.readline().split()))     #정수

cards.sort()

for n in nums:
    start = bisect_left(cards, n)
    en = bisect_right(cards, n)  
    l = en-start
    print(l, end=' ') 