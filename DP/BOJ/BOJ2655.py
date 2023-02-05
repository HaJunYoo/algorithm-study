n = int(input())
bricks = []
for i in range(n):
    a, b, c = map(int, input().split())
    bricks.append((a, b, c, i+1))
bricks.sort(key = lambda x : x[0], reverse=True)
# print(bricks)
dy = [0] * n
dy[0] = bricks[0][1]
res = bricks[0][1]

for i in range(1, n):
    max_h = 0
    for j in range(i - 1, -1, -1):
        if bricks[j][2] > bricks[i][2] and dy[j] > max_h:
            max_h = dy[j]
    dy[i] = max_h + bricks[i][1]
    res = max(res, dy[i])
# print(res)

res = max(dy)
index = n-1
history = []
while res > 0:
    if dy[index] == res:
        history.append(bricks[index][3])
        res -= bricks[index][1]
        # print(res)
    index -= 1

# print(history)
print(len(history))
for elem in history:
    print(elem)
