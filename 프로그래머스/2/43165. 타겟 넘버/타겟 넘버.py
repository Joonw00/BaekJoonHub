def solution(numbers, target):
    answer = 0
    def cnt(numbers,i,tot, target):
        nonlocal answer
        if i <len(numbers):
            cnt(numbers,i+1,tot+numbers[i], target)
            cnt(numbers,i+1,tot-numbers[i], target)
        else:
            if tot == target:
                answer+=1
    cnt(numbers,0,0,target)
    return answer

    