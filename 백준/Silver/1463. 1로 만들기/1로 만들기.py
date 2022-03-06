N = input()
N = int(N)
d = [0] * (N + 1)

for id in range(1, N+1): #d의 인덱스 id
    if id+1 <N+1:
        if d[id+1] == 0 or d[id+1] > d[id]+1:
            d[id+1] = d[id] +1
    if 3*id < N+1:
        if d[3*id] == 0 or d[3*id] > d[id]+1:
            d[3*id] = d[id] +1
    if 2*id < N + 1:
        if d[2*id] == 0 or d[2*id] > d[id]+1:
            d[2*id] = d[id] +1
print(d[N])
    