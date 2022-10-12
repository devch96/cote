def solution(numbers, direction):
    if direction == "left":
        pop = numbers.pop()
        numbers.insert(0,pop)
        return numbers
    else:
        pop = numbers.pop(0)
        numbers.append(pop)
        return numbers
