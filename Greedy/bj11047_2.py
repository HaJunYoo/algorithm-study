N, K = map(int, input().split())

coins = [int(input()) for _ in range(N)]

num = 0

coins.sort(reverse = True)

for coin in coins :
	while K >= coin :
		num += K // coin
		K %= coin

print(num)