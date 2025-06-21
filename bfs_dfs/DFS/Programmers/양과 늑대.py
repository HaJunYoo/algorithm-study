from collections import defaultdict


def solution(info, edges):
    visited = [False for _ in range(len(info))]
    answer = list()

    def dfs(sheep, wolf):
        if sheep > wolf:
            answer.append(sheep)
        else:
            return

        for p, c in edges:
            if visited[p] and not visited[c]:
                visited[c] = True
                if info[c] == 0:
                    dfs(sheep + 1, wolf)
                else:
                    dfs(sheep, wolf + 1)
                visited[c] = False

    visited[0] = True
    dfs(1, 0)

    return max(list(set(answer)))


if __name__ == '__main__':
    infos = [[0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1],
             [0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0]]

    edges_set = [
        [[0, 1], [1, 2], [1, 4], [0, 8], [8, 7], [9, 10], [9, 11], [4, 3], [6, 5], [4, 6], [8, 9]],
        [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [4, 8], [6, 9], [9, 10]]
    ]

    answers = [5, 5]

    for index, (info, edges) in enumerate(zip(infos, edges_set)):

        ans = solution(info, edges)
        try:
            assert ans == answers[index], f'ans={ans}'
            print(ans)
        except ValueError as e:
            raise e
