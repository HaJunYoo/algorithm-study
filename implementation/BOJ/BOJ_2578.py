def visit_check(target, graph, visited):
    for x in range(5):
        for y in range(5):
            if target == graph[x][y]:
                visited[x][y] = True
                return visited
        
            
def bingo_check(visited):
    cnt = 0
    
    # 가로 체크
    for i in range(5):
        dx = 0
        for j in range(5):
            if visited[i][j]:
                dx += 1
        if dx == 5:
            cnt += 1
    
    # 세로 체크
    for i in range(5):
        dy = 0
        for j in range(5):
            if visited[j][i]:
                dy += 1
        if dy == 5:
            cnt += 1
            
    # 대각선 체크
    d1 = 0
    for i in range(5):
        if visited[i][i]:
            d1 += 1
    if d1 == 5:
        cnt += 1

    d2 = 0
    for i in range(5):
        if visited[i][4-i]:
            d2 += 1
    if d2 == 5:
        cnt += 1

    if cnt >= 3:
        return True
    else:
        return False
        



if __name__ == '__main__':
    
    graph = []
    for _ in range(5):
        graph.append(list(map(int, input().split())))
    bingo = []
    for _ in range(5):
        bingo.extend(list(map(int, input().split())))
    visited = []
    for __ in range(5):
        visited.append([False]*5)
    
    cnt = 0
    res = 0
    flag = False
    for i in range(25):
        visited = visit_check(bingo[i], graph, visited)
        cnt += 1
                
                
        if cnt >= 12:
            if bingo_check(visited):
                # print(cnt, "빙고")
                # res = cnt
                print(cnt)
                exit()

    
