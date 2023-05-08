T = int(input())
answerList = []
def factorize(n):
    factor = 2 #시작 소수 지정
    factors = []
    while (factor**2 <= n):  
        while (n % factor == 0):  
            factors.append(factor)  
            n = n // factor  
        factor += 1
    if n > 1 : 
        factors.append(n)
    return factors

for test_case in range(1,T+1):
    A = int(input())
    counter = dict()
    measure = factorize(A)
    answer = 1
    
    for num in set(measure):
        counter[num] = measure.count(num)
    
    for n, cnt in counter.items():
        if cnt % 2 != 0 :
            answer *= n
    answerList.append([test_case,answer])

for test_case, answer in answerList:
    print(f'#{test_case} {answer}')