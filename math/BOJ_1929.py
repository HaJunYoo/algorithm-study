# max = 1000000
#
# check = [False]*(max+1)
# check[0] = check[1] = True
#
# for i in range(2, max+1):
#     if not check[i]:
#         j = i+i
#         while j <= max :
#             check[j] = True
#             j += i
#
# m, n = map(int, input().split())
# numbers = [x for x in range(m, n + 1)]
#
# for num in numbers:
#     if not check[num] :
#         print(num)

m, n = map(int, input().split())

ch = [False]*(n+1)
ch[0] = ch[1] = True

for i in range(2, n+1):
    if not ch[i]:
        temp = i+i
        for j in range(temp, n+1, i):
            ch[j] = True
# print(ch)

numbers = [x for x in range(m, n + 1)]
for num in numbers:
    if not ch[num] :
        print(num)