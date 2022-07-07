import sys
INF = 1000000007
n,k = map(int,sys.stdin.readline().split())
def sqr(a,b):
    #종료 조건
    if b == 0:
        return 1
    elif b == 1:
        return a
    temp = sqr(a,b//2)
    if b%2 == 1:
        return temp*temp*a % INF
    else:
        return temp*temp%INF
fact = []
fact.append(1)
fact.append(1)
for i in range(2,n+1):
    temp = fact[-1]
    temp = (temp*i)%INF
    fact.append(temp)
up = fact[n] #분자
und = fact[k] * fact[n-k] #분모
und = und%INF #??

rev = sqr(und,INF-2)
rev = rev%INF
ans = (up*rev)%INF
print(ans)