n = int(input())

direction = list(map(str, input().split()))

# 동 북 서 남
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

# 현재 위치 => (1,1)
x, y = 1, 1

def move(dir):

    global x, y

    if dir == "R":
        nx = x + dx[0]
        ny = y + dy[0]
    elif dir == "U" :
        nx = x + dx[1]
        ny = y + dy[1]
    elif dir == "L":
        nx = x + dx[2]
        ny = y + dy[2]
    else :
        nx = x + dx[3]
        ny = y + dy[3]

    return nx, ny


for direct in direction:
    nx, ny = move(direct)
    if nx < 1 or ny < 1 or nx > n or ny > n :
        continue # 아래의 코드를 실행하지 않고 건너 뜀

    x, y = nx, ny

print(f'{x} {y}')


'''
5
R R R U D D
'''