import sys
n = int(sys.stdin.readline())

word = []
for i in range(n):
    temp = sys.stdin.readline().strip()
    word.append(temp)

for i in word:
    # [::-1] 으로 글자 거꾸로.
    if i[::-1] in word:
        ans = i
        break
l = len(ans)

ans = ans[l//2]

print(l, ans)