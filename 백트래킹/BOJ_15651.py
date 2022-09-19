n, m = map(int, input().split())

numbers = list()

def print_numbers():
    for num in numbers :
        print(num, end=" ")
    print()

def choose(cnt):
    if cnt == m :
        print_numbers()
        return

    for i in range(1, n+1):
        numbers.append(i)
        choose(cnt+1)
        numbers.pop()

choose(0)