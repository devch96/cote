def solution(n):
    count = 0
    
    def isPrime(n):
        if n == 1:
            return False
        if n == 2 or n == 3:
            return True
        for i in range(2,int(n**0.5)+1):
            if n % i == 0:
                return False
        return True
    for i in range(2, n+1):
        if isPrime(i):
            count +=1
    return count

"""
num = set(range(2,n+1))
for i in range(2,int(n**0.5)+1):
    if i in num:
        num -= set(range(2*i,n+1,i)
return len(num)
"""
