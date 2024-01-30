from collections import deque
from typing import List


def isBipartite(graph: List[List[int]]) -> bool:
    color = [-1 for _ in range(len(graph))]
    for i, c in enumerate(color):
        if c == -1:
            queue = deque([i])
            color[i] = 0
            while queue:
                cur_v = queue.popleft()
                for next_v in graph[cur_v]:
                    # not visited
                    if color[next_v] == -1:
                        print('color[cur_v]', color[cur_v])
                        color[next_v] = color[cur_v] ^ 1
                        print('next_v', color[next_v])
                        queue.append(next_v)
                    elif color[next_v] == color[cur_v]:
                        return False
    return True



if __name__ == '__main__':
    graph = [[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]]
    print(isBipartite(graph))