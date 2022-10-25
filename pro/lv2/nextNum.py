def solution(n):
    a = bin(n).count('1')
    n += 1
    while bin(n).count('1') != a:
        n += 1
    return n

print(solution(78))
