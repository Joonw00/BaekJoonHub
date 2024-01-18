import sys

n = int(sys.stdin.readline().strip())
tot = 0
ans = set()
for i in range(n):
    chat = sys.stdin.readline().strip()
    if chat == 'ENTER':
        tot += len(ans)
        ans = set()
        continue
    ans.add(chat)

tot += len(ans)
print(tot)