def solution(n):
    answer = 0
    f = 0
    l = 0
    tot = 0
    while f<=n:
        if tot<n:
            l+=1
            tot+=l
        elif tot>n:
            f+=1
            tot-=f
        else:
            answer+=1
            f+=1
            tot-=f
    return answer