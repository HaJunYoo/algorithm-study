import copy

def fill(graph:list, direction:list, x:int, y:int) -> None:
    
    for d in direction:
        nx, ny = x, y
    
        # 이동할 수 없을 때까지 이동하면서 '#'으로 변경
        while True:
            nx += dx[d]
            ny += dy[d]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                break
            if graph[nx][ny] == 6:
                break
            elif graph[nx][ny] == 0:
                graph[nx][ny] = '#'
        

def dfs(depth:int, graph:list) -> None:
    global min_val, direction
    
    temp = copy.deepcopy(graph) # 각 깊이별 graph 초기화
    
    # cctv 전부 조회한 후 사각지대(0)의 개수 세기
    if depth == len(cctv):
        count = 0
        for t in temp:
            count += t.count(0)
        min_val = min(min_val, count)
        return
    
    # cctv 하나 씩 조회
    cctv_num, x, y = cctv[depth]
    # cctv 방향에 맞는 dir 조회
    for dir in direction[cctv_num]:
        fill(temp, dir, x, y)
        dfs(depth+1, temp)
        temp = copy.deepcopy(graph) # 이전 그래프로 초기화
        


if __name__ == '__main__':
    
    n, m = map(int, input().split())
    
    cctv = []
    graph = []
    for i in range(n):
        data = list(map(int, input().split()))
        graph.append(data)
        for j in range(m):
            if data[j] in [1, 2, 3, 4, 5]:
                cctv.append([data[j], i, j]) # cctv 타입, x, y
            
                
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    
    ## cctv가 바라볼 수 있는 타입 정의
    direction = {
    1: [[0], [1], [2], [3]],
    2: [[0, 2], [1, 3]],
    3: [[0, 1], [1, 2], [2, 3], [3, 0]],
    4: [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]],
    5: [[0, 1, 2, 3]]
    }   
    
    
    min_val = int(1e9)
    
    dfs(0, graph)
    print(min_val)
    
    
    
    
    
    