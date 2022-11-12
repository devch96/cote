from collections import deque
def solution(prices):
    prices = deque(prices)
    answer = []
    while prices:
        count = 0
        n = prices.popleft()
        for i in prices:
            count +=1
            if n > i:
                break
        answer.append(count)
    return answer
print(solution([1,2,3,2,3]))
        

