def solution(price, money, count):
    total = price * sum([i for i in range(1,count+1)])
    if money - total >= 0:
        return 0
    return total - money

"""
return max(0,price*(count+1)*count // 2 - money)
"""
