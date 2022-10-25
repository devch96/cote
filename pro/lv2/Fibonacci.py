def solution(n):
    def fibonacci(s):
        if s == 1 or s == 2:
            return 1
        else:
            return fibonacci(s-1) + fibonacci(s-2)

    def fib(s):
        a , b = 1 , 1
        if s == 1 or s == 2:
            return 1
        else:
            for i in range(1,s):
                a, b = b , a+b
        return a



    return fib(n)%1234567
