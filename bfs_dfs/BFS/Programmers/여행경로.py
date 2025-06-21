from copy import deepcopy

tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]
n = len(tickets)

graph = dict()
for t in tickets:
    dp, ds = t
    # 출발지 기준
    graph[dp] = graph.get(dp, list()) + [ds]

for r in graph:
    graph[r].sort(reverse=True)

stack = ["ICN"]
path = []
while stack:
    print(stack)
    top = stack[-1]
    # stack에서 끝 노드(출발지)가 출발지 목록에 없거나 이미 연결된 목적지를 다 방문했을 때
    if top not in graph or len(graph[top]) == 0:
        path.append(stack.pop())
    else:
        stack.append(graph[top][-1])
        graph[top].pop()
# print(path)
path = path[::-1]
# print(path)

