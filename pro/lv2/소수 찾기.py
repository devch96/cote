from itertools import permutations
def is_prime(num):
    if num == 1 or num == 0:
        return False
    if num == 2:
        return True
    else:
        for i in range(2, int(num**0.5)+1):
            if num % i == 0:
                return False
    return True

def solution(numbers):
    answer = 0
    temp = set()
    for i in range(1,len(numbers)+1):
        for j in permutations(numbers,i):
            temp.add(int(''.join(j)))
    for n in temp:
        if is_prime(n):
            answer += 1
    return answer

print(solution("011"))
print(solution("17"))
