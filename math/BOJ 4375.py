# BOJ 10430
# BOJ 4375 => 1

# 1로만 이루어진 N의 배수 중 길이가 최소인 것을 찾는
# N의 배수는 N을 나눈 나머지가 0이다

# Bottom up 방식으로


def solve():
    num = 0
    i = 1

    while True:
        num = num * 10 + 1
        num %= n
        if num == 0:
            print(i)
            break
        i += 1

while True :
    try:
        n = int(input())
        solve()
    except:
        break
