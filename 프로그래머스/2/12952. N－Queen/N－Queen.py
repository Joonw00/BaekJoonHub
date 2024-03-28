def backtracking(row_used, col_used, diag1_used, diag2_used, depth, limit):
    global count
    if depth == limit:
        count += 1
        return
    for i in range(limit):
        if not col_used[i] and not diag1_used[depth + i] and not diag2_used[depth - i + limit - 1]:
            row_used[depth] = i
            col_used[i] = diag1_used[depth + i] = diag2_used[depth - i + limit - 1] = True
            backtracking(row_used, col_used, diag1_used, diag2_used, depth + 1, limit)
            col_used[i] = diag1_used[depth + i] = diag2_used[depth - i + limit - 1] = False

def solution(n):
    global count
    count = 0
    row_used = [0] * n
    col_used = [False] * n
    diag1_used = [False] * (2 * n - 1)
    diag2_used = [False] * (2 * n - 1)
    backtracking(row_used, col_used, diag1_used, diag2_used, 0, n)
    return count
