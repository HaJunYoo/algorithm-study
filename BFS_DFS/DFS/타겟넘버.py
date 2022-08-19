numbers = [1, 1, 1, 1, 1]

target = 3
#############

n = len(numbers)

number_list = list()

# print(number_list)

res = 0

product = (1, -1)

def dfs(cnt):
    global res, target

    if cnt == n:
        temp = sum(number_list)
        # print(temp)
        if temp == target :
            res += 1
        return

    # cnt 증가 시키는 loop
    for j in range(2) :
        number_list.append((product[j] * numbers[cnt]))
        # print(number_list)
        dfs(cnt+1)
        number_list.pop()
        # print(number_list)

dfs(0)

print(res)
