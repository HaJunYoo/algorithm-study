n, m = map(int, input().split())

currency = [int(input()) for _ in range(n)]

memoization = [0] * (n+1)

currency.sort(reverse=True)

for idx, coin in enumerate(currency) :
    if m >= coin :
        memoization[idx] = m // coin

        m = m % coin
        # print(m)

if m != 0 :
    print(-1)
else :
    print(sum(memoization))

# print(memoization)