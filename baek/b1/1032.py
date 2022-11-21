n = int(input())
temp = []
for i in range(n):
    temp.append(input())
first = list(temp[0])
for i in range(n):
    for j in range(len(first)):
        if first[j] == temp[i][j]:
            continue
        else:
            first[j] = "?"
print(''.join(first))