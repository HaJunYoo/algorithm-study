from collections import deque
from itertools import combinations
from copy import deepcopy

dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

# virus bfs
def virus_bfs(new_graph:list, virus_queue:deque) -> list:
    while virus_queue:
        x, y = virus_queue.popleft()
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0<=nx<n and 0<=ny<m:
                if new_graph[nx][ny] == 0:
                    new_graph[nx][ny] = 2
                    virus_queue.append((nx, ny))
                    
    return new_graph

def count_graph(new_graph:list) -> int:
    cnt = 0
    for line in new_graph:
        # print(line)
        cnt += line.count(0)    
    # print(cnt)
    # print()
    return cnt


if __name__ == '__main__':

    n, m = map(int,input().split())
    graph = []
    max_cnt = -12800000

    for _ in range(n):
        temp = list(map(int, input().split()))
        graph.append(temp)

    virus = deque()
    vacant = list()

    # 0:빈칸 1:벽 2: 바이러스
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 2:
                virus.append((i, j))
            if graph[i][j] == 0:
                vacant.append((i, j))


    for comb in combinations(vacant, 3):
            
        new_graph = deepcopy(graph)
        new_virus = deepcopy(virus)
        
        for spot in comb:
            x, y = spot
            new_graph[x][y] = 1

        new_graph = virus_bfs(new_graph=new_graph, virus_queue=new_virus)

        cnt = count_graph(new_graph=new_graph)
        if cnt > max_cnt:
            max_cnt = cnt

    print(max_cnt)