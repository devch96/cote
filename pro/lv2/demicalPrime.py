def solution(n,k):
    def demical(num, s):
        result = ""
        while num>0:
            num, mod = divmod(num,s)
            result += str(mod)
        return result[::-1]

    def isPrime(s):
        if s == 1:
            return False
        if s == 2:
            return True
        for i in range(2,int(s**0.5)+1):
            if s % i == 0:
                return False
        return True

    count = 0
    temp = demical(n,k)
    for i in temp.split('0'):
        if i == '':
            continue
        if isPrime(int(i)):
            count += 1
    return count