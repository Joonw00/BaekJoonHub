def solution(s):
    answer = []
    l = len(s)
    for i in range(l):
        answer.append(-1)
        for j in range(i):
            if s[j] == s[i]:
                answer[-1] = i-j
                
    return answer