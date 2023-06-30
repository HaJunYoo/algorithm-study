import heapq

def dijkstra(graph:dict, start:int) -> dict:
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    queue = []
    heapq.heappush(queue, [distances[start], start])
    
    # print(distances)
    while queue:
        current_distance, current_dest = heapq.heappop(queue)
        # print(f'{current_distance} {current_dest}')
        
        if distances[current_dest] < current_distance:
            continue
        
        for new_dest, new_distance in graph[current_dest].items():
            temp_distance = current_distance + new_distance
            if temp_distance < distances[new_dest]:
                distances[new_dest] = temp_distance
                heapq.heappush(queue, [temp_distance, new_dest])
    
    return distances
            


if __name__ == '__main__':
    v, e = map(int, input().split())
    
    graph = dict()
    for i in range(1, v+1):
        graph[i] = dict()
    
    k = int(input())
    edges = []
    
    for _ in range(e):
        u, v, w = map(int, input().split())
        graph[u][v] = w
        edges.append((u, v, w))
    
    # print(graph)
    distances = dijkstra(graph=graph, start=k)
    
    for node, distance in distances.items():
        if distance == float('inf'):
            print('INF')
            # print(type(distance))
        else:
            print(distance)
            
    # print(distances)
    
    