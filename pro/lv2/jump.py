def solution(n):
    def fib(s):
        a,b = 1, 1
        if s == 1 or s == 2:
            return 1
        else:
            for i in range(1,s):
                a, b = b, a+b
        return a
    return fib(n+1)%1234567
