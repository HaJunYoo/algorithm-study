n = int(input())

remain = 1000 - n

coins = [500, 100, 50, 10, 5, 1]
i = 0
cnt = 0

while True:
    if i >= len(coins):
        break

    if coins[i] <= remain:
        mok = remain // coins[i]
        remain %= coins[i]
        cnt += mok
        # print(coins[i], remain, mok, cnt)
    else:
        i += 1

print(cnt)