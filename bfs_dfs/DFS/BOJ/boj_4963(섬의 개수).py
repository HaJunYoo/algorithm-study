import sys
sys.setrecursionlimit(10**6)
# input = sys.stdin.readline

# 상하좌우
dxs1, dys1 = (-1, 1, 0, 0), (0, 0, -1, 1)
# 대각선
dxs2, dys2 = (1, -1, 1, -1), (1, -1, -1, 1)


def coord_valid(x, y):
    if x < 0 or x > h - 1 or y < 0 or y > w - 1:
        return False
    else:
        return True


def dfs(x, y):

    if arr[x][y] == 0:
        return False

    if not visited[x][y] and arr[x][y] == 1:
        visited[x][y] = True

        for dx, dy in zip(dxs1, dys1):
            nx = x + dx
            ny = y + dy
            if coord_valid(nx, ny):
                dfs(nx, ny)

        for dx, dy in zip(dxs2, dys2):
            nx = x + dx
            ny = y + dy
            if coord_valid(nx, ny):
                dfs(nx, ny)

        return True

    return False


if __name__ == "__main__":

    flag1 = True

    while flag1:

        w, h = map(int, input().split())
        # print(w, h)

        if w == 0 and h == 0:
            flag1 = False
            break

        arr = []
        for _ in range(h):
            temp = list(map(int, input().split()))
            arr.append(temp)

        # print(arr)

        visited = [[False] * w for _ in range(h)]
        # print(visited)

        result = 0
        for i in range(h):
            for j in range(w):
                if dfs(i, j):
                    result += 1

        print(result)

'''
1 1
0
2 2
0 1
1 0
3 2
1 1 1
1 1 1
5 4
1 0 1 0 0
1 0 0 0 0
1 0 1 0 1
1 0 0 1 0
5 4
1 1 1 0 1
1 0 1 0 1
1 0 1 0 1
1 0 1 1 1
5 5
1 0 1 0 1
0 0 0 0 0
1 0 1 0 1
0 0 0 0 0
1 0 1 0 1
0 0
'''