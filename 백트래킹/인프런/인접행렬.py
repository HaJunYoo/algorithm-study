n, m = map(int, input().split())
mat = [[0]*(n) for _ in range(n)]

for _ in range(m):
    a, b, c = map(int, input().split())
    mat[a-1][b-1] = c

for elem in mat:
    for e in elem:
        print(e, end = ' ')
    print()

