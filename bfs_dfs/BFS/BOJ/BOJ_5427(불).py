from collections import deque

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def burn():
    flen = len(fire)
    for _ in range(flen):
        x, y = fire.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < c and 0 <= ny < r:
                if graph[nx][ny] != '#' and graph[nx][ny] != '*':
                    graph[nx][ny] = '*'
                    fire.append((nx, ny))

def move():
    cango = False
    jlen = len(jihun)
    for _ in range(jlen):
        x, y = jihun.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < c and 0 <= ny < r:
                if visited[nx][ny] == 0 and graph[nx][ny] != '*' and graph[nx][ny] != '#' and graph[nx][ny] == '.':
                    cango = True
                    visited[nx][ny] = visited[x][y] + 1
                    jihun.append((nx, ny))
            else:
                return visited[x][y]            
    if not cango:
        return 'IMPOSSIBLE'


if __name__ == '__main__':
    
    T = int(input())

    for _ in range(T):
        r, c = map(int, input().split())
        graph = []
        visited = [[0] * r for _ in range(c)]
        fire = deque()
        jihun = deque()

        for i in range(c):
            graph.append(list(map(str, input().strip())))
            for j in range(r):
                if graph[i][j] == '*':
                    fire.append((i, j))
                if graph[i][j] == '@':
                    jihun.append((i, j))
                    visited[i][j] = 1
                    
        result = 0
        while True:
            burn()
            result = move()
            if result:
                break

        print(result)