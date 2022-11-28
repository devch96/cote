import sys
input = sys.stdin.readline
t = int(input())
deque=[]
for _ in range(t):
    cmd = input().strip()
    if cmd.split()[0] == "push_front":
        deque.insert(0, cmd.split()[1])
    elif cmd.split()[0] == "push_back":
        deque.append(cmd.split()[1])
    elif cmd == "pop_front":
        print(deque.pop(0) if deque else -1)
    elif cmd == "pop_back":
        print(deque.pop() if deque else -1)
    elif cmd == "size":
        print(len(deque))
    elif cmd == "empty":
        print(0 if deque else 1)
    elif cmd == "front":
        print(deque[0] if deque else -1)
    elif cmd == "back":
        print(deque[-1] if deque else -1)
