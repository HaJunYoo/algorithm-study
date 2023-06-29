from collections import deque
# reverse = O(n) -> for loop 안에 갇히면 시간 복잡도가 10만*10만이 되어버린다
def lingual(func, numbers, n):
    number = deque(numbers)

    if n == 0:
        print("error")

    else:
        # reverse flag가 홀수이면 loop가 끝나고 뒤집는다
        # flag ---

        reverse_flag = 0

        for char in func:
            if char == "R":
                reverse_flag += 1
            elif char == "D":
                if len(number) < 1:
                    print("error")
                    break
                else:
                    if (reverse_flag % 2) == 1:
                        number.pop()
                    elif (reverse_flag % 2) == 0:
                        number.popleft()

        if (reverse_flag % 2) == 1:
            number.reverse()

        if len(number) != 0:
            temp = '[' + ','.join(map(str, number)) + ']'
            print(temp)


t = int(input())

for i in range(t):
    p = input()
    n = int(input())
    numbers = list(input()[1:-1].split(','))
    lingual(p, numbers, n)


