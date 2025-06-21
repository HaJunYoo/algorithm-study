import sys
sys.setrecursionlimit(10 ** 6)
# sys.stdin=open("input.txt", "r")

def valid_coord(x, y):
    if 0 <= x < m and 0 <= y < n:
        return True
    else:
        return False


def print_array(array):
    for elem in array:
        print(elem)


def bfs():
    while queue:
        # tmp_len = len(queue)
        # for _ in range(tmp_len):
        temp = queue.popleft()
        temp_dis = dis[temp[0]][temp[1]]
        for dx, dy in zip(dxs, dys):
            nx = temp[0] + dx
            ny = temp[1] + dy
            # 익지 않은 상태이거나 유효한 좌표일 때
            if valid_coord(nx, ny) and arr[nx][ny] == 0:
                queue.append((nx, ny))
                arr[nx][ny] = 1
                dis[nx][ny] = temp_dis + 1


if __name__ == '__main__':

    from collections import deque

    n, m = map(int, input().split())

    arr = []
    for _ in range(m):
        arr.append(list(map(int, input().split())))

    dis = []
    for _ in range(m):
        dis.append([0] * n)

    dxs = (-1, 1, 0, 0)
    dys = (0, 0, -1, 1)
    # print_array(arr)
    # print('----')
    # print_array(dis)

    queue = deque()
    for i in range(m):
        for j in range(n):
            if arr[i][j] == 1:
                queue.append((i, j))

    bfs()
    # print_array(dis)

    # arr에서 0을 발견하면 flag = False로 설정
    flag = True
    for i in range(m):
        for j in range(n):
            if arr[i][j] == 0:
                flag = False

    result = 0
    if not flag:
        print(-1)
    else:
        for i in range(m):
            for j in range(n):
                if dis[i][j]>result:
                    result=dis[i][j]

        print(result)

'''
6 4
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 1
'''