def dfs(k, graph, visited):
    visited[k] = 1
    for i in range(len(graph[k])):
        if visited[i] == 0 and graph[k][i] == 1:
            dfs(i, graph, visited)

def solution(n, computers):
    dxs, dys = (0, 0, 1, -1), (1, -1, 0, 0)
    
    visited = [0]*n
    answer = 0

    for i in range(n):
        if visited[i] == 0:
            # print(f"{i} {j}")
            dfs(i, computers, visited)
            answer += 1
    
    print(answer)
    return answer


if __name__ == '__main__':
    computers = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    for elem in computers:
        print(elem)
    n = 3
    solution(n, computers)
    