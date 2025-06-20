n, k = map(int, input().split())
nums = list(map(int, input().split()))
numbers = []
visited = [False] * (n + 1)
m = int(input())
res = 0


def combination(level, start):
    global res

    if level == k:
        # print(numbers, end=' ')
        if sum(numbers) % m == 0:
            res += 1
            # print('정답')
        # print()
        return

    for i in range(start, n):
        if not visited[i]:
            visited[i] = True
            numbers.append(nums[i])
            combination(level + 1, i + 1)
            numbers.pop()
            visited[i] = False


combination(0, 0)
print(res)
