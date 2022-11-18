n, m = map(int, input().split())

res = 0


def permutation(cnt, num):
    global res

    if cnt == m:
        res += 1
        print(num.strip())
        return

    for i in range(1, n + 1):
        permutation(cnt + 1, num + " " + str(i))


permutation(0, "")
print(res)
