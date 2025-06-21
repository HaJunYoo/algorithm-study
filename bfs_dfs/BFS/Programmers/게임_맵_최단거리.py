from collections import deque

def bfs(dis, maps, n, m):
    dxs, dys = (-1, 1, 0, 0), (0, 0, -1, 1)
    q = deque()
    q.append((0,0))
    dis[0][0] = 1
    
    while q:
        x, y = q.popleft()
        # print(f'{x} {y}')
        for dx, dy in zip(dxs, dys):
            nx, ny = x+dx, y+dy
            if 0 <= nx < n and 0 <= ny < m:
                if maps[nx][ny] == 1:
                    if dis[nx][ny] > dis[x][y] + 1 or dis[nx][ny] == 0:
                        q.append((nx, ny))
                        dis[nx][ny] = dis[x][y] + 1
                else:
                    continue
    return dis

def solution(maps):

    n = len(maps)
    m = len(maps[0])
    
    dis = [[0]*m for _ in range(n)]
    # print(dis)
    dis = bfs(dis, maps, n, m)
        
    if dis[n-1][m-1] == 0:
        return -1
    else:
        return dis[n-1][m-1]

if __name__ == '__main__':
    maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1],[0,0,0,0,1]]
    answer = solution(maps)
    print(answer)