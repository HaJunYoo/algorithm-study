n = int(input())

direction = list(map(str, input().split()))

# 동 북 서 남
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

move_types = {"R" : 0, "U" : 1, "L" : 2, "D" : 3}

# 현재 위치 => (1,1)
x, y = 1, 1

def move(dir):

    global x, y

    move_num = move_types[dir]

    nx = x + dx[move_num]
    ny = y + dy[move_num]

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