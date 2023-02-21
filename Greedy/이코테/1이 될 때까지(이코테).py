n, k = map(int, input().split())

result = 0
print(n)
while n%k != 0:

    n -= 1
    result += 1
    print(n)

while True:
    n //= k
    result += 1
    print(n)
    if n == 1:
        break

print(result)