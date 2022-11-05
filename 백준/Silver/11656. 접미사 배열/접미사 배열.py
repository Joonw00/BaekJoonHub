s = input()
ans = []
for i in range(len(s)):
    ans.append(s[i:])
ans.sort()
for i in ans:
    print(i)