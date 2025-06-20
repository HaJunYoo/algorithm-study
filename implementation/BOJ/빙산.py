from collections import deque

def bfs(x_0, y_0, graph, visited, count):
    dxs, dys = (-1,1,0,0), (0,0,-1,1)
    q = deque()
    q.append([x_0, y_0])
    visited[x_0][y_0] = True
    while q:
        x_1, y_1 = q.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny = x_1+dx, y_1+dy
            if 0<=nx<n and 0<=ny<m:
                if not visited[nx][ny]:
                    if graph[nx][ny] > 0:
                        q.append([nx, ny])
                        visited[nx][ny] = True
                    elif graph[nx][ny] == 0:
                        count[x_1][y_1] += 1
                    
    return visited
                    
        
def search(graph, count):
    visited = [[False]*m for _ in range(n)]
    cnt = 0
    for x in range(n):
        for y in range(m):
            if not visited[x][y]:
                if graph[x][y] > 0:
                    visited = bfs(x, y, graph, visited, count)
                    cnt += 1
    # print(cnt)
    return cnt
    
    

if __name__ == '__main__':
    n, m = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(n)]
    
    dxs, dys = (-1,1,0,0), (0,0,-1,1)
    year = 0
    flag = False
    while True:
        # print(graph)
        # print()
        count = [[0]*m for _ in range(n)]
        res = search(graph, count)
        
        if res >= 2:
            flag = True
            # print('2개 이상으로 분리')
            break
        
        if max(max(graph)) == 0:
            # print('다 녹았음')
            break
        
        
        for x in range(n):
            for y in range(m):
                graph[x][y] = max(graph[x][y]-count[x][y],0)
        
        year += 1
        
        
    # print('year :', year)

    if not flag:
        print(0)
    else:
        print(year)
    
'''
5 7
0 0 0 0 0 0 0
0 2 4 5 3 0 0
0 3 0 2 5 2 0
0 7 6 2 4 0 0
0 0 0 0 0 0 0


5 7
0 0 0 0 0 0 0
0 0 0 0 0 0 0
0 0 0 1 0 0 0
0 0 0 0 0 0 0
0 0 0 0 0 0 0
'''