import sys
input = sys.stdin.readline
lt = []
t = int(input())
for _ in range(t):
    cmd = input().strip()
    if cmd.split()[0] == 'push':
        lt.append(cmd.split()[1])
    elif cmd == "pop":
        print(lt.pop(0) if lt else -1)
    elif cmd == "size":
        print(len(lt))
    elif cmd == "empty":
        print(0 if lt else 1)
    elif cmd == "front":
        print(lt[0] if lt else -1)
    elif cmd == "back":
        print(lt[-1] if lt else -1)
