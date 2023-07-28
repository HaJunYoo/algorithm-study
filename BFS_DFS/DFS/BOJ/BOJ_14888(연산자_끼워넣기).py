def dfs(depth:int, n:int, result:int):
    global max_num, min_num
    # print('현재 ',result)
    
    if depth == n:
        # print(result)
        max_num = max(result, max_num)
        min_num = min(result, min_num)
        return

    for i in range(4):
        if operators[i] > 0:
            # print(i)
            temp = operatoration(result, numbers[depth], i)
            # print(temp)
            operators[i] -= 1
            dfs(depth+1, n, temp)
            operators[i] += 1
            
                

def operatoration(a, b, number):
    if number == 0:
        return a+b
    elif number == 1:
        return a-b
    elif number == 2:
        return a*b
    elif number == 3:
        return int(a/b)


if __name__ == '__main__':
    n = int(input())
    numbers = list(map(int, input().split()))
    # 0: 덧셈 1: 뺄셈 2:곱셈 3: 나눗셈
    operators = list(map(int, input().split()))
    # print(operators)
    # 1e9
    max_num = -12800000000
    min_num = 128000000000
    
    dfs(1, n, numbers[0])
    print(max_num)
    print(min_num)

    