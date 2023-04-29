if __name__ == '__main__':

    n = int(input())
    target = int(input())
    center = (n//2, n//2)

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
            if graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y]+1
                x, y = nx, ny
                dir_count += 1
            else:
                dir_count -= 1
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


            
            
            
            
        
    
    
    
