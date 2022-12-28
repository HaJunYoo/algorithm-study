n = int(input())
days = [tuple(map(int, input().split())) for _ in range(n)]
max_sum = -2170000

# print(days)

def dfs(cur, sum):
    global max_sum

    # if sum < max_sum:
    #     return

    if cur > n-1:
        if sum > max_sum:
            max_sum = sum
        return

    schedule = days[cur]
    T = schedule[0]
    P = schedule[1]

    dfs(cur+T, sum+P)
    dfs(cur+1, sum)


dfs(0, 0)

print(max_sum)