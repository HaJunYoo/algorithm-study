from itertools import combinations

small = []

for _ in range(9):
    small.append(int(input()))

small.sort(reverse=True)

ans = list()

one, two = 0, 0

for elem in combinations(small, 2) :
    if (sum(small) - sum(elem)) == 100 :
        one, two = elem
        break

small.remove(one)
small.remove(two)

small.sort()

for person in small :
    print(person)