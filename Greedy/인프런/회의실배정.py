n = int(input())

s = []

for _ in range(n):
    a, b = map(int, input().split())
    s.append((a,b))

# s.sort(key = lambda x: (x[1], abs(x[1]-x[0])))
s.sort(key = lambda x: (x[1], x[0]))
# print(s)
# [(2, 3), (1, 4), (3, 5), (4, 6), (5, 7)]

start = 0
end = 0
cnt = 0

for a, b in s:
    # print(a, b)
    if end <= a:
        start = a
        end = b
        # print(start, end)
        cnt += 1

print(cnt)