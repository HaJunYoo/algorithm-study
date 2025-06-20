n, m = map(int, input().split())
visited = [False] * (n + 1)
numbers = []
res = 0

def combination(cnt, start):
    global res
    if cnt == m:
        res += 1
        for elem in numbers:
            print(elem, end=' ')
        print()
        return

    for i in range(start, n + 1):
        if not visited[i]:
            numbers.append(i)
            visited[i] = True
            combination(cnt + 1, i + 1)
            visited[i] = False
            numbers.pop()

        else:
            continue


combination(0, 1)
print(res)
