n = int(input())

graph = []
dp = [[0]*n for _ in range(n)]

for _ in range(n):
    graph.append(list(map(int, input().split())))

# print(graph)

dp[0][0] = graph[0][0]

for i in range(1, n):
    for j in range(i):
        dp[i][j] = max(dp[i][j], dp[i-1][j] + graph[i][j])
        dp[i][j+1] = max(dp[i][j+1], dp[i-1][j] + graph[i][j+1])
        # print(f'{i} {j}')
    
print(max(dp[-1]))