import sys

def checkSize(name):
    large = 0
    small = 0
    ans = 0
    for i in range(len(name)):
        if name[i] >= 'a' and name[i] <='z':
            small +=1
        elif name[i] >= 'A' and name[i] <='Z':
            large+=1
    if large<=small:
        ans  = 1
    return ans
def lengthUnder10(name):
    ans = 0
    if len(name) <= 10:
        ans = 1
    return ans


n = int(input())
for i in range(n):
    name = sys.stdin.readline().strip() 
    if checkSize(name) and lengthUnder10(name) and not name.isdigit():
        print(name)
