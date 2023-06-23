from collections import deque
from copy import deepcopy

def bfs(x_0, y_0, graph, visited):
    dxs, dys = (-1,1,0,0), (0,0,-1,1)
    q = deque()
    q.append([x_0, y_0])
    visited[x_0][y_0] = True
    while q:
        x_1, y_1 = q.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny = x_1+dx, y_1+dy
            if 0<=nx<n and 0<=ny<m:
                if not visited[nx][ny] and graph[nx][ny] > 0:
                    q.append([nx, ny])
                    visited[nx][ny] = True
    
    return visited
                    
        
def search(graph):
    visited = [[False]*m for _ in range(n)]
    cnt = 0
    for x in range(n):
        for y in range(m):
            if not visited[x][y]:
                if graph[x][y] > 0:
                    visited = bfs(x, y, graph, visited)
                    cnt += 1
    # print(cnt)
    return cnt
    
    

if __name__ == '__main__':
    n, m = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(n)]

    dxs, dys = (-1,1,0,0), (0,0,-1,1)
    year = 0
    flag = False
    while year<500:
        # print(graph)
        # print()
        res = search(graph)
        if res >= 2:
            flag = True
            # print('2개 이상으로 분리')
            break
        
        if max(max(graph)) == 0:
            # print('다 녹았음')
            break
            
        temp = deepcopy(graph)
        for x in range(n):
            for y in range(m):
                if graph[x][y] > 0:
                    cnt = 0
                    for dx, dy in zip(dxs, dys):
                        nx, ny = x+dx, y+dy
                        if 0<=nx<n and 0<=ny<m:
                            if graph[nx][ny] == 0:
                                cnt+=1
                    temp_cnt = temp[x][y] - cnt
                    temp_cnt = max(temp_cnt, 0)
                    temp[x][y] = temp_cnt
                    
        graph = temp
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