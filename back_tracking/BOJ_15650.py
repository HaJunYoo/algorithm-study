# n, m = map(int, input().split())
#
# numbers = list()
#
# visited = [False]*(n+1)
#
# def choose(cnt):
#     if cnt == m :
#         for elem in numbers :
#             print(elem, end = " ")
#         print()
#         return
#
#     for i in range(1, n+1):
#         if not visited[i] :
#             # 리스트 원소가 1개 이상이고 이번에 추가하려는 원소가 직전에 추가한 것보다 클 때
#             if len(numbers) != 0 and numbers[-1] < i :
#                 numbers.append(i)
#                 visited[i] = True
#                 # print(numbers)
#                 choose(cnt+1)
#                 numbers.pop()
#                 visited[i] = False
#
#             elif len(numbers) == 0 :
#                 numbers.append(i)
#                 visited[i] = True
#                 # print(numbers)
#                 choose(cnt + 1)
#                 numbers.pop()
#                 visited[i] = False
#
#
#         else :
#             continue
#
# choose(0)
##############################
### 강의 풀의 보고 ##############

n, m = map(int, input().split())

numbers = list()

visited = [False]*(n+1)

def choose(cnt, start):
    if cnt == m :
        for elem in numbers :
            print(elem, end = " ")
        print()
        return


    for i in range(start, n+1):
        if not visited[i] :
            # 리스트 원소가 1개 이상이고 이번에 추가하려는 원소가 직전에 추가한 것보다 클 때
            numbers.append(i)
            visited[i] = True
            # print(numbers)
            # 다음 재귀에서는 현재 i보다 1 더 큰 값부터 loop를 돈다
            choose(cnt+1, i+1)
            numbers.pop()
            visited[i] = False

        else :
            continue

choose(0, 1)