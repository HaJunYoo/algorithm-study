if __name__ == '__main__':

    n = int(input())
    target = int(input())
    center = (n//2, n//2) # 실수한 부분 가운데는 //2로 구해야 한다.

    graph = [[0]*n for _ in range(n)]
    dxs, dys = (-1, 0, 1, 0), (0, 1, 0, -1)
    # graph[center[0]][center[1]] = 1

    x, y = center[0], center[1]
    dir_count = 0
    graph[x][y] = 1
    res = ''
    while (x, y) != (0, 0):
        # print(f'{x} {y}')
        # print(graph[x][y])
        dir = dir_count % 4
        # print(f'방향 {dir}')
        # print(dir_count)
        dx, dy = dxs[dir], dys[dir]
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < n:
            # 방문하지 않은 경우
            if graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y]+1
                x, y = nx, ny
                dir_count += 1
            # 방문했을 경우 이동하지 않고 이전 방향으로 바꿔놓는다.
            else:
                dir_count -= 1
        # 유효성 검증에 통과 못할 경우 시계 방향으로 튼다.
        else:
            dir_count += 1
            

    for elem in graph:
        for e in elem:
            print(e, end=' ')
        print()


    for i in range(n):
        for j in range(n):
            if graph[i][j] == target:
                print(f'{i+1} {j+1}')
                exit()
            
        
    
    
    
