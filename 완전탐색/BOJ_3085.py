# 시간 복잡도는 O(N^4) => 26만번 정도 loop는 python 기준 1초 안에 끝난다.
dx, dy = (1, 0), (0, 1)

n = int(input())
a = list()
for _ in range(n):
    a.append([s for s in input()])

# print(candies)

def search() :
    ans = 1

    for i in range(n):
        cnt = 1

        # 행 탐색
        for j in range(1, n):
            if a[i][j] == a[i][j-1] :
                cnt += 1
            else :
                cnt = 1

        if ans < cnt :
            ans = cnt

        # 열 탐색
        for j in range(1, n) :
            if a[j][i] == a[j-1][i] :
                cnt += 1
            else :
                cnt = 1

        if ans < cnt :
            ans = cnt

    return ans



def in_range(x, y):
    if 0 <= x and x < n and 0 <= y and y < n :
        return True
    else :
        return False


ans = 0
for i in range(n) :
    for j in range(n) :
        for idx in range(2) :
            temp_x = i + dx[idx]
            temp_y = j + dy[idx]
            if in_range(temp_x, temp_y) :
                # swap
                a[i][j] , a[temp_x][temp_y] = a[temp_x][temp_y], a[i][j]

                temp = search()

                # 최대 개수가 temp가 더 많다면 갱신
                if ans < temp :
                    ans = temp
                # swap 원상 복귀
                a[i][j] , a[temp_x][temp_y] = a[temp_x][temp_y], a[i][j]

print(ans)