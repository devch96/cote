def solution(price):
    answer = price
    if 100000 <= price < 300000:
        answer = price*0.95
    elif 300000 <= price < 500000:
        answer = price*0.9
    elif price >= 500000:
        answer = price*0.8
    return int(answer)

"""
discount_rates = {500000:0.8, 300000:0.9, 100000:0.95}
for discount_price, discount_rate in discount_rates.item():
    if price >= discount_price:
        return int(price * discount_rate)
"""
