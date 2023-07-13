
if __name__ == '__main__':
    
    n, m, k, x = map(int, input().split())
    link = [[] for _ in range(n+1)]
    
    # 링크드 리스트 구현 
    for _ in range(m):
        a, b = map(int, input().split())
        link[a].append(b)
    
    start_node = x
    dis = [0]*(n+1)
    visited = [False]*(n+1)
    
    def bfs(start_node, target_dis) -> list:
        from collections import deque
        
        answer = []
        queue = deque()
        visited[start_node] = True
        queue.append(start_node)
        dis[start_node] = 0
        
        
        while queue:
            now = queue.popleft()
            for next in link[now]:
                if not visited[next]:
                    visited[next] = True
                    queue.append(next)
                    dis[next] = dis[now] + 1
                    
                    if dis[next] == target_dis:
                        answer.append(next)
    
        return answer
    
    answer = bfs(start_node=start_node, target_dis=k)

    
    if len(answer) == 0:
        print(-1)
    else:
        #
        answer.sort()
        for ans in answer: print(ans)

        
        
    