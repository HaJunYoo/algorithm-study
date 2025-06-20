# t = int(input())
#
# numbers = []
# for _ in range(t):
#     numbers.append(tuple(map(int, input().split())))
#
# # print(numbers)
# def calculate(tuple):
#
#     m, n, x, y = tuple
#     year = []
#     a = 1
#     b = 1
#     year.append((a, b))
#
#     for i in range(2, (m*n+1)):
#
#         a += 1
#         b += 1
#         if a == m+1 :
#             a = 1
#         if b == n+1 :
#             b = 1
#
#         year.append((a, b))
#         # print((a, b))
#
#     if (x, y) in year:
#         temp = year.index((x, y)) + 1
#     else:
#         temp = -1
#
#     # print(temp)
#
#     return temp
#
# for tuple in numbers :
#     ans = calculate(tuple)
#     print(ans)

#
#
# t = int(input())
#
# for _ in range(t):
#     m, n, x, y = map(int, input().split())
#     x -= 1
#     y -= 1
#     # k는 년도
#     # 어떤 k가 정답인지 알아보기 위해서 k를 m으로 나눈 나머지가 x
#     k = x
#     while k < n*m :
#         #
#         if k % n == y :
#             print(k+1)
#             break
#         k += m # k를 m으로 나눈 나머지가 x
#
#     else :
#         print(-1)

'''
3
10 12 3 9
10 12 7 2
13 11 5 6
'''

t = int(input())

numbers = []
for _ in range(t):
    numbers.append(tuple(map(int, input().split())))

def calculate(tuple):
    M, N, x, y = tuple
    k = x

    f = True

    while (k <= (M * N)):

        if k % N == y % N:
            return k
            f = False
            break
        k += M

    if f:
        return -1


for tuple in numbers :
    ans = calculate(tuple)
    print(ans)