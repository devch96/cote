def solution(skill, skill_trees):
    answer = 0
    for i in skill_trees:
        check = "".join([x for x in i if x in skill])
        if skill.startswith(check):
            answer +=1
    return answer
print(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"]
))