'''
풀이 전략:
첫 행을 탐색하면서 DFS 탐색을 한다
이 때 탐색 방향은 좌, 우, 아래 방향만 탐색하게 한다
이 때, 탐색 우선 순위는 좌, 우 -> 아래
좌 우가 있을 때는 좌 우로 가고 그 외에는 아래로 가면 된다
이 때 만약 마지막 행에 도착했을 때 숫자가 2일 경우, 출발 지점을 리턴해준다

아니었다...
거꾸로 탐색을 해야했던 문제
2를 찾아서 2부터 역으로 DFS를 해야하는 문제
'''
import sys
sys.setrecursionlimit(10 ** 6)
# sys.stdin = open("in1.txt", "r")

# 좌표, 시작지점
def dfs(x, y):
    print(f'{x}, {y}')
    visited[x][y] = True

    if x == 0:
        print(y)
        sys.exit(0)
        return


    if 0 <= y - 1 < n and arr[x][y - 1] == 1 and not visited[x][y - 1]:
        dfs(x, y - 1)

    elif 0 <= y + 1 < n and arr[x][y + 1] == 1 and not visited[x][y + 1]:
        dfs(x, y + 1)

    else:
        dfs(x-1, y)



if __name__ == '__main__':
    n = 10
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().split())))
    visited = [[False]*n for _ in range(n)]

    # print(arr[9][5])

    for i in range(n):
        if arr[9][i] == 2:
            # print('start')
            dfs(9, i)
