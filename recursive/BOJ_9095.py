n = int(input())

sum_list = list()

def summation(cnt, num):
    global ans

    # 불가능한 경우
    if sum(sum_list) > num :
        return

    # 정답인 경우
    if sum(sum_list) == num:
        # print(sum_list)
        ans += 1
        return

    # 최대 탐색했지만 없는 경우는 리턴
    if cnt == num:
        return

    for i in range(1, 4):
        sum_list.append(i)
        summation(cnt + 1, num)
        sum_list.pop()


numbers = [int(input()) for _ in range(n)]

for num in numbers:
    ans = 0
    summation(0, num)
    print(ans)