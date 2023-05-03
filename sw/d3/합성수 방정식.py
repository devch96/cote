def isPrime(n):
    if n == 2 or n == 3:
        return True
    else:
        for i in range(2,int(n**0.5)+1):
            if n % i == 0:
                if i == n//i:
                    return True
                return False
    return True

T = int(input())
for test_case in range(1,T+1):
    N = int(input())
    y = 2
    x = y+N
    while True:
        if not isPrime(x) and not isPrime(y):
            print(f'#{test_case} {x} {y}')
            break
        x+=1
        y+=1



