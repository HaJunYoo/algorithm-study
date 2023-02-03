import sys
sys.setrecursionlimit(10**6)

n = int(input())
arr = []
for _ in range(n):
    temp = input()
    arr.append([int(num) for num in temp])

dxs, dys = (-1, 1, 0, 0), (0, 0, -1, 1)

# visited = [[False] * n for _ in range(n)]

# print(arr)
# print(visited)

def valid_coord(x, y):
    if 0 <= x < n and 0 <= y < n:
        return True
    else:
        return False


# 1인 부분을 전부 탐색한 후 다 탐색하면 True를 return하는 함수
def dfs(x, y):
    global cnt

    if arr[x][y] == 0:
        return False

    if arr[x][y] == 1:
        arr[x][y] = 0
        cnt += 1

        for dx, dy in zip(dxs, dys):
            nx = x + dx
            ny = y + dy
            if valid_coord(nx, ny):
                dfs(nx, ny)

        return True

    return False


cnt_arr = []
arr[0][0] = 0
for i in range(n):
    for j in range(n):
        cnt = 0
        if dfs(i, j):
            cnt_arr.append(cnt)

# print(arr)
print(len(cnt_arr))
cnt_arr.sort()
for elem in cnt_arr:
    print(elem)
# print(cnt_arr)
