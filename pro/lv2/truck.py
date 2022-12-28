from collections import deque
def solution(bridge_length, weight, truck_weights):
    count = 0
    bridge = deque([0]*bridge_length, maxlen=bridge_length) 
    truck_weights = deque(truck_weights)
    ing = 0
    while truck_weights or ing != 0:
        count += 1
        ing -= bridge[0]
        if truck_weights and ing + truck_weights[0] <= weight:
            ing += truck_weights[0]
            bridge.append(truck_weights.popleft())
        else:
            bridge.append(0)
    return count
print(solution(2,10,[7,4,5,6]))
print(solution(100,100,[10]))
print(solution(100,100,[10,10,10,10,10,10,10,10,10,10]))