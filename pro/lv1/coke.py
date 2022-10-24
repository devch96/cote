def solution(a, b, n):
    answer = 0
    while n >= a:
       x, y = divmod(n,a) 
       x *= b
       answer += x
       n = x+y
    return answer
print(solution(2,1,20))
print(solution(3,1,20))

