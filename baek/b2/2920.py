a = list(map(int,input().split()))
asc = sorted(a)
desc = sorted(a, reverse=True)
if a == asc:
    print("ascending")
elif a == desc:
    print("descending")
else:
    print("mixed")