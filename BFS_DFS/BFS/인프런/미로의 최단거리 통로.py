from collections import deque

a = []
for _ in range(7):
    a.append(list(map(int, input().split())))

dis = [[0] * 7 for _ in range(7)]
visited = [[False] * 7 for _ in range(7)]

dx, dy = (1, -1, 0, 0), (0, 0, -1, 1)


def valid_ck(x, y):
    if 0 <= x < 7 and 0 <= y < 7:
        return True
    else:
        return False


queue = deque()
queue.append((0, 0))
visited[0][0] = True
cnt = 0
x, y = 0, 0

while True:

    for _ in range(len(queue)):
        current = queue.popleft()
        x, y = current

        print(cnt)

        if x == 6 and y == 6:
            break

        for i in range(4):
            new_x = x + dx[i]
            new_y = y + dy[i]

            if valid_ck(new_x, new_y):
                if not visited[new_x][new_y] and a[new_x][new_y] != 1:
                    visited[new_x][new_y] = True
                    dis[new_x][new_y] = dis[x][y] + 1
                    queue.append((new_x, new_y))

    if x == 6 and y == 6:
        break

# 최단 거리
print(dis[6][6])
for c in dis:
    print(c)

# 총 탐색한 횟수
print(cnt)

'''
0 0 0 0 0 0 0
0 1 1 1 1 1 0
0 0 0 1 0 0 0
1 1 0 1 0 1 1
1 1 0 1 0 0 0
1 0 0 0 1 0 0
1 0 1 0 0 0 0
'''