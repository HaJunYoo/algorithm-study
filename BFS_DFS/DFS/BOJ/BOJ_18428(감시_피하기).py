def check_student():
    # 학생을 찾으면 True
    flag = False
    
    for teacher in teachers:

        for i in range(4):
            x, y = teacher
            dx, dy = directions[i]
            
            while True:
                x = x + dx
                y = y + dy
                if 0<=x<n and 0<=y<n:
                    if graph[x][y] == 'S':
                        flag = True
                        break
                    elif graph[x][y] == 'O':
                        break
                else:
                    break
                    
    return flag
                
                
def dfs(cnt):
    global res, candid_len
    
    if cnt == 3:
        flag = check_student()
            
        if not flag:
            # print('YES')
            res += 1
            
        return
    
    else:
        for i in range(candid_len):
            if not visited[i]:
                x, y = candid[i]
                graph[x][y] = 'O'
                visited[i] = True
                dfs(cnt+1)
                visited[i] = False
                graph[x][y] = 'X'


if __name__ == '__main__':
    n = int(input())
    graph = []
    for _ in range(n):
        graph.append(list(map(str, input().split())))

    candid = []
    teachers = []
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 'X':
                candid.append((i, j))
            elif graph[i][j] == 'T':
                teachers.append((i, j))


    directions = [(0,1), (0,-1),(1,0),(-1,0)]

    candid_len = len(candid)
    visited = [False]*candid_len

    res = 0

    dfs(0)
    if res > 0:
        print('YES')
    else:
        print('NO')
