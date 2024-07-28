def solution(n):
    answer = []

    def dfs(n, src, target, inter):
        if n == 1:
            answer.append([src, target])
        else:
            dfs(n - 1, src, inter, target)
            dfs(1, src, target, inter)
            dfs(n - 1, inter, target, src)

    dfs(n, 1, 3, 2)

    return answer