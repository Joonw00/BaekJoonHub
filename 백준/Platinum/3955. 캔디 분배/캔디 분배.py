import sys
T = input()
T = int(T)

#if gcd(c,k) != 1 : IMPOSSIBLE출력
#ans*C ≡ 1 mod K

def eea(a,b):
  s0 = 1
  s1 = 0
  t0 = 0
  t1 = 1
  K = b
  while b:
    q = a//b
    r = a%b
    a = b
    b = r
    temp = s0
    s0 = s1
    s1 = temp - s1*q
    temp = t0
    t0 = t1
    t1 = temp - t1*q
  if a!=1:
    return 10**9 + 1
  s0 = (s0 % K + K) % K
  return s0


for i in range(T):
  K,C = map(int, sys.stdin.readline().split())
  if C == 1:
    #이거 없어도 되지 않나
    if K+1 > 10**9:
      print("IMPOSSIBLE")
      continue
    print(K+1)
    continue
  if K == 1:
    print(1)
    continue
  ans = eea(C,K)
  if ans>10**9:
    print("IMPOSSIBLE")
    continue

  print(ans)
