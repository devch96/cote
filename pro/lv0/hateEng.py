def solution(numbers):
    eng = {"zero":"0","one":"1","two":"2","three":"3","four":"4","five":"5","six":"6","seven":"7","eight":"8","nine":"9"}
    for word, num in eng.items():
        numbers = numbers.replace(word,num)
    answer = int(numbers)
    return answer

"""
for num, eng in enumerate(["zero","~~~]):
    numbers = numbers.replace(eng, str(num))
return int(numbers)
"""

