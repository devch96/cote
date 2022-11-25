n = int(input())
for i in range(n):
    stack = []
    str = input()
    for x in str:
        if x == "(":
            stack.append(x)
        else:
            if stack:
                stack.pop()
            else:
                print("NO")
                break
    else:
        if stack:
            print("NO")
        else:
            print("YES")