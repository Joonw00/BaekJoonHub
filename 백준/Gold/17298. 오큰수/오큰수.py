import sys
N = input()
N = int(N)
A = list(map(int, sys.stdin.readline().split()))
ans = [0]*N
st = []
st.append(A[0])
#작아졌으면 추가
#커졌으면 pop
for i in range(1,N):
  i = int(i)
  if A[i-1] >= A[i]:
    st.append(A[i])
  else:
    #j 계산에서 에러뜸
    j = i-1
    while st and j>=0:
      if A[i]<=st[-1]:
        break
      if ans[j] != 0:
        j-=1
        continue
      st.pop()
      ans[j] = A[i]
      j-=1
    st.append(A[i])



for i in range(N):
  if ans[i] == 0:
    print(-1,end=" ")
  else:
    print(ans[i],end=" ")