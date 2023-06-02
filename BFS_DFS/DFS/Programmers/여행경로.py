from collections import defaultdict

def dfs(graph, path, visit):
    
    if path:
        # print(path)
        # 최근 방문한 지점
        to = path[-1]
        # 지점 기준 연결된 곳이 있으면 알파벳 순서가 빠른 곳 방문
        if graph[to]: path.append(graph[to].pop(0))
        # 연결된 곳이 없을경우, path의 가장 뒤부터 pop 하여 visit에 쌓는다
        else: 
            elem = path.pop()
            # print(elem)
            visit.append(elem)
        dfs(graph, path, visit)
    
    
    return path, visit[::-1]

def solution(tickets):
    path = ["ICN"]
    graph = defaultdict(list)
    for a, b in tickets:
        graph[a].append(b)
    for key in graph.keys():
        graph[key].sort()
    
    path, visit = dfs(graph=graph, path = path, visit=[])
    print(path)
    print(visit)
    # print(visit[::-1])
    return visit

if __name__ == "__main__":
    tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]
    solution(tickets)