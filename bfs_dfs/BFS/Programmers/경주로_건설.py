from collections import deque

def bfs(board:list, init_path:int):
    direc = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    n = len(board)
    
    dis = [[12800000]*n for _ in range(n)]
    queue = deque()
    queue.append([0, 0, 0, init_path])
    dis[0][0] = 0
    
    
    while queue:
        x, y, cost, path = queue.popleft()
        for i in range(4):
            nx = x + direc[i][0]
            ny = y + direc[i][1]
            
            if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == 0:
                
                if path == i: new_cost = cost + 100
                else: new_cost = cost + 600
                
                if dis[nx][ny] > new_cost:
                    queue.append([nx, ny, new_cost, i])                    
                    dis[nx][ny] = new_cost
                
            else:
                continue
                    
    return dis[n-1][n-1]


def solution(board):
    
    min_val = min([bfs(board=board, init_path=i) for i in range(1, 3)])
    
    return min_val

if __name__ == '__main__':
    board = [[0,0,1,0],[0,0,0,0],[0,1,0,1],[1,0,0,0]]
    answer = solution(board=board)
    print(answer)