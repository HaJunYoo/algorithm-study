# 나이트가 이동할 수 있는 방향 벡터
steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

def dfs():

    global min_val

    queue = list()
    # 시작점
    queue.append((a, b))

    while queue :
        # 가장 오른쪽에 있는 것 pop
        x, y = queue.pop()

        # 이동 카운트가 기록된 최솟값 min_val보다 많을 때는 탐색 중지
        if visited[x][y] > min_val:
            continue

        # 도착했을 때
        if x == c and y == d :

            if visited[x][y] < min_val:
                min_val = visited[x][y]

        for step in steps :
            nx = x + step[0]
            ny = y + step[1]

            # 유효성 검증  0 ~ n-1
            if nx < 0 or ny < 0 or nx >= n or ny >= n :
                continue


            if not visited[nx][ny] :

                visited[nx][ny] = visited[x][y] + 1

                queue.append((nx, ny))






test_num = int(input())

for _ in range(test_num):
    n = int(input())
    a, b = map(int, input().split())
    c, d = map(int, input().split())

    visited = [[0] * n for _ in range(n)]

    min_val = float('inf')

    dfs()

    print(min_val)





