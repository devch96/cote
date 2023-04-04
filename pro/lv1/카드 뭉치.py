from collections import deque
def solution(cards1, cards2, goal):
    cards1, cards2, goal = deque(cards1), deque(cards2), deque(goal)
    for s in goal:
        if len(cards1) and s == cards1[0]:
            cards1.popleft()
        elif len(cards2) and s == cards2[0]:
            cards2.popleft()
        else:
            return "No"
    return "Yes"

print(solution(["i", "drink", "water"],["want", "to"],["i", "want", "to", "drink", "water"]))
print(solution(["i", "water", "drink"],["want", "to"],["i", "want", "to", "drink", "water"]))