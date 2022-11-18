def print_numbers():
    for elem in numbers:
        print(elem, end=" ")
    print()

def subset(cnt):
    global n

    if cnt == n + 1:
        if len(numbers) == 0:
            return
        else:
            print_numbers()
        return

    numbers.append(cnt)
    # print(numbers)
    subset(cnt + 1)
    numbers.pop()

    subset(cnt + 1)
    # print(numbers)


n = int(input())
numbers = []

# 1 2 3
# 4 exit
subset(1)
