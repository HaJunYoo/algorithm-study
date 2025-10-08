from itertools import permutations

mans = []
for _ in range(9):
    mans.append(int(input()))

ans = []
for man in permutations(mans, 7):
    if sum(man) == 100:
        ans.extend(man)
        break

for a in ans:
    print(a)

