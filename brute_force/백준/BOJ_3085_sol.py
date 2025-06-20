def check():
    ans = 1

    for k in range(n):
        cnt = 1

        # 행 탐색
        for l in range(1, n):
            if a[k][l] == a[k][l - 1]:
                cnt += 1
            else:
                cnt = 1

        if ans < cnt:
            ans = cnt

        # 열 탐색
        for l in range(1, n):
            if a[l][k] == a[l - 1][k]:
                cnt += 1
            else:
                cnt = 1

        if ans < cnt:
            ans = cnt

    return ans

n = int(input())
a = [list(input()) for _ in range(n)]
ans = 0

for i in range(n):
    for j in range(n):
        if j+1 < n:
            a[i][j],a[i][j+1] = a[i][j+1],a[i][j]
            temp = check()
            if ans < temp:
                ans = temp
            a[i][j],a[i][j+1] = a[i][j+1],a[i][j]

        if i+1 < n:
            a[i][j],a[i+1][j] = a[i+1][j],a[i][j]
            temp = check()
            if ans < temp:
                ans = temp
            a[i][j],a[i+1][j] = a[i+1][j],a[i][j]
print(ans)