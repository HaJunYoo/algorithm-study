def count_bomb(i, j, bombs, located, res, flag):
    if bombs[i][j] == '*' and located[i][j] == 'x':
                flag = True
            
    elif located[i][j] == 'x' and bombs[i][j] != '*':
        for dx, dy in zip(dxs, dys):
            nx, ny = i+dx, j+dy
            if 0 <= nx < n and 0 <= ny < n: 
                if bombs[nx][ny] == '*':
                    res[i][j] += 1
        
        res[i][j] = str(res[i][j])
    
    elif located[i][j] == '.':
        res[i][j] = '.'
        
    else:
        res[i][j] = str(res[i][j])
    
    
    return flag, res


if __name__ == '__main__':
    n = int(input())
    bombs = [[char for char in input()] for _ in range(n)]
    located = [[char for char in input()] for _ in range(n)]
    res = [[0]*n for _ in range(n)]

    dxs, dys = (-1, 1, 0, 0, -1, 1, -1, 1), (0, 0, -1, 1, -1, 1, 1, -1)

    flag = False
    for i in range(n):
        for j in range(n):
            flag, res = count_bomb(i, j, bombs, located, res, flag)
            
            
    if flag:
        for i in range(n):
            for j in range(n):
                if bombs[i][j] == '*':
                    res[i][j] = '*'

    for elem in res:
        print(''.join(elem))
