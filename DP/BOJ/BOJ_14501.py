# n = int(input())
# array = [(0, 0)]
# for _ in range(n):
#     array.append(tuple(map(int, input().split())))
#
# ans = 0
# end = n
#
# for idx in range(1, n + 1):
#     temp = 0
#
#     while idx <= end:
#         if (idx + array[idx][0]) <= n+1:
#             temp += array[idx][1]
#             idx += array[idx][0]
#
#         else:
#             idx += 1
#
#     if ans < temp:
#         ans = temp
#
# print(ans)

n = int(input())
array = [(0, 0)]
for _ in range(n):
    array.append(tuple(map(int, input().split())))

ans = 0

def summation(idx, sum):
    global ans

    if idx > n :
        if sum > ans :
            ans = sum
        return

    if (idx + array[idx][0]) <= n+1:
        summation(idx + array[idx][0], sum+array[idx][1])
        summation(idx+1, sum)

    else :
        summation(idx + 1, sum)

summation(1, 0)
print(ans)