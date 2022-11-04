import heapq
def solution(phone_book):
    if len(phone_book) == 1:
        return True
    heapq.heapify(phone_book)
    answer = True
    p_num = heapq.heappop(phone_book)
    while phone_book:
        i = 0
        if phone_book[i].startswith(p_num):
            return False
        p_num = heapq.heappop(phone_book)
        i+=1
    return answer

"""
answer = True
hash_map = {}
for phone_number in phone_book:
    hash_map[phone_number] = 1
for phone_number in phone_book:
    temp = ""
    for number in phone_number:
        temp += number
        if temp in hash_map and temp != phone_number:
            answer = False
return answer
"""