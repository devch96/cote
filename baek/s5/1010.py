def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result
T = int(input())
for i in range(T):
    n, m = map(int, input().split())
    count = factorial(m) // (factorial(m-n) * factorial(n))
    print(count)
