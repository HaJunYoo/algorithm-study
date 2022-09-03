# 시간 복잡도는 O(N^4) => 26만번 정도 loop는 python 기준 1초 안에 끝난다.
dx, dy = (1, 0), (0, 1)

n = int(input())
candies = list()
for _ in range(n):
    candies.append([s for s in input()])

print(candies)

x, y = 0, 0

def in_range(x, y):
    if 0 <= x < n and 0 <= y < n :
        return True
    else :
        return False

def search() :
    ans = 1

    for k in range(n):
        cnt = 1

        # 행 탐색
        for l in range(1, n):
            if candies[k][l] == candies[k][l-1] :
                cnt += 1
            else :
                cnt = 1

        if ans < cnt :
            ans = cnt

        # 열 탐색
        for l in range(1, n) :
            if candies[l][k] == candies[l-1][k] :
                cnt += 1
            else :
                cnt = 1

        if ans < cnt :
            ans = cnt

    return ans


ans = 0
for i in range(n) :
    for j in range(n) :
        for idx in range(2) :
            temp_x = i + dx[idx]
            temp_y = j + dy[idx]
            if in_range(temp_x, temp_y) and candies[i][j] != candies[temp_x][temp_y] :
                # swap
                candies[i][j] , candies[temp_x][temp_y] = candies[temp_x][temp_y], candies[i][j]

                temp = search()

                # 최대 개수가 temp가 더 많다면 갱신
                if ans < temp :
                    ans = temp
                # swap 원상 복귀
                candies[i][j] , candies[temp_x][temp_y] = candies[temp_x][temp_y], candies[i][j]




print(ans)
