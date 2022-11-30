n, m = map(int, input().split())
visited = [False] * (n + 1)
numbers = []
res = 0


def same(i, cnt, start):
    numbers.append(i)
    visited[i] = True
    combination(cnt + 1, start + 1)
    visited[i] = False
    numbers.pop()


def combination(cnt, start):
    global res
    if cnt == m:
        res += 1
        for elem in numbers:
            print(elem, end=' ')
        print()
        return

    for i in range(start, n + 1):
        if len(numbers) != 0:
            if not visited[i] and numbers[-1] < i:
                same(i, cnt, start)

            else:
                continue
        else:
            if not visited[i]:
                same(i, cnt, start)

            else:
                continue


combination(0, 1)
print(res)
