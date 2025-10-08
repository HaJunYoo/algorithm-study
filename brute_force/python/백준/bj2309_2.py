from itertools import combinations

lst = [int(input()) for _ in range(9)]

tmp = ()

for elem in combinations(lst, 7) :
	if sum(elem) == 100 :
		tmp = elem

tmp = list(tmp)
tmp.sort()

for i in tmp :
	print(i)