def solution(a,b):
    month = [31, 29, 31, 30,31, 30, 31, 31, 30, 31, 30, 31]
    days = ["FRI","SAT","SUN","MON","TUE","WED","THU"]
    if a > 1 :
        total = sum(month[0:a])+b-1
    elif a == 1:
        total = b-1
    answer = days[total%7]
    return answer

