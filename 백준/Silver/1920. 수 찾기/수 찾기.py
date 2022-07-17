from bisect import bisect_left, bisect_right
import sys
def b_search(arr, target):
    left = bisect_left(arr, target)
    return left< len(arr) and arr[left] == target
n = input()
n = int(n)
A = list(map(int, input().split()))
M = input()
M = int(M)
B = list(map(int, input().split()))
A.sort()
for i in B:
    if b_search(A, i):
        print(1)
    else:
        print(0)