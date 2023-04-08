def solution(keymap, targets):
    answer = []
    for target in targets:
        cnt, flag = 0, True
        for s in target:
            minIdx = min([101] + [k.find(s)+1 for k in keymap if k.find(s) != -1])
            if minIdx == 101:
                flag = False
                break
            cnt += minIdx
        answer.append(cnt if flag else -1)
    return answer

print(solution(["ABACD", "BCEFD"],["ABCD","AABB"]))
