from collections import deque
 
n = int(input())
graph = [[0] * n for _ in range(n)]
graph[0][0] = 1

k = int(input())
for _ in range(k):
    a, b = map(int, input().split())
    graph[a - 1][b - 1] = 2

l = int(input())
turns = deque()
for _ in range(l):
    x, c = input().split()
    x = int(x)
    turns.append((x, c))


directions = [(0, 1), (-1, 0), (0, -1), (1, 0)]
direction_index = 0

def turn(c, direction_index):
    if c == 'D':
        direction_index -= 1
    else:
        direction_index += 1
    
    return (direction_index % 4)

# 'L':+1 , 'D':-1
res = 0
x, y = 0, 0
queue = deque()
queue.append((0, 0))

while True:
    res += 1
    dx, dy = directions[direction_index]
    
    nx = x + dx
    ny = y + dy
    
    if nx < 0 or nx >= n or 0 or ny < 0 or ny >= n:
        break
        
    # 꼬리가 지나간 부분 deque를 통해 처리 필요
    if graph[nx][ny] == 2:
        graph[nx][ny] = 1
        queue.append((nx, ny))
    
    elif graph[nx][ny] == 0:
        graph[nx][ny] = 1
        queue.append((nx, ny))
        tx, ty = queue.popleft()
        graph[tx][ty] = 0
        
    else:
        break
    
    if turns:
        if turns[0][0] == res:
            t, c = turns.popleft()
            direction_index = turn(c, direction_index)
    
    x, y = nx, ny
    

print(res)

    
    






