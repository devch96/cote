n = int(input())
team = [input()[0] for i in range(n)]
first = set(team)
member = []
for i in first:
    if team.count(i) >= 5:
        member.append(i)
if member:
    print(''.join(sorted(member)))
else:
    print("PREDAJA")