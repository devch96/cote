def solution(s):
     answer = []
     for i in s.split(" "):
        if i == "Z":
            answer.pop()
        else:
            stack.append(int(n))

     return sum(answer)
