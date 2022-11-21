import sys
n = int(sys.stdin.readline())
st = []
for i in range(n):
    a,b,c,d = sys.stdin.readline().split()
    b = int(b)
    c = int(c)
    d = int(d)
    st.append([d,c,b,a])
st.sort(reverse=True)
print(st[0][3])
print(st[-1][3])