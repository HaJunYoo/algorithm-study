import sys
import itertools as it

n, f = map(int, input().split())
b = [1] * n
cnt = 0

for i in range(1, n):
    b[i] = b[i - 1] * (n - i) // i
# print(b)

a = list(range(1, n + 1))
for tmp in it.permutations(a):
    s = 0
    # print(tmp)
    for x, y in zip(tmp, b):
        s += x*y
    # print(s)

    if s == f:
        for elem in tmp:
            print(elem, end=' ')
        print()
        sys.exit(0)


