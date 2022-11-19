n = int(input())
coins = list(map(int, input().split()))
remain = int(input())
coins.sort(reverse=True)

cnt = float("inf")


def remainder(dep, sum):
    global cnt

    if dep >= cnt or sum > remain:
        return

    if sum == remain:
        if dep < cnt:
            print(f'{dep} {sum}')
            cnt = dep
        return

    else:
        for coin in coins:
            temp = sum+coin
            # print(temp)
            remainder(dep + 1, temp)


remainder(0, 0)
print(cnt)