def solution(s):
    answer = ''
    s = s.upper()
    answer += s[0]
    for i in range(len(s)-1):
        if s[i] != ' ':
            answer+=s[i+1].lower()
        else:
            answer+=s[i+1]
    return answer