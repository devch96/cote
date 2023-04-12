def solution(n):
    c = 0
    s = 1
    for _ in range(n):
        c , s = s, c+s
    return s
print(solution(4))
