t = int(input())

n_list = [int(input()) for _ in range(t)]

def count(target ,sum, cnt):

    global ans

    # print(sum)

    if sum == target :
        ans += 1
        # print("---------------정답------------------")
        return

    if cnt == target :
        return

    for i in range(1, 4):
        # 더해준다
        count(target, sum+i, cnt+1)
        # # 더하지 않는다
        # count(target, sum, cnt+1)


for num in n_list :
    ans = 0
    count(num, 0, 0)
    print(ans)

# num = int(input())
#
# ans = 0
#
# count(num, 0, 0)
#
# print(ans)