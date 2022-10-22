def solution(nums):
    def isPrime(n):
        if n == 1:
            return False
        if n == 2 or n == 3:
            return True
        for i in range(2,int(n**0.5)+1):
            if n % i == 0:
                return False
        return True
    answer = 0
    for x in range(len(nums)):
        for y in range(x+1, len(nums)):
            for z in range(y+1, len(nums)):
                if isPrime(nums[x]+nums[y]+nums[z]):
                    answer += 1
    return answer
