n, m = map(int, input().split())

numbers = list(map(int, input().split()))

numbers.sort()

choose_list = list()

visited = [False]*(n+1)


def print_number():
    for elem in choose_list:
        print(elem, end = " ")
    print()

def choose(cnt):
    if cnt == m :
        print_number()
        return

    for i in range(n):
        if not visited[i] :
            visited[i] = True
            choose_list.append(numbers[i])
            choose(cnt+1)
            choose_list.pop()
            visited[i] = False

        else :
            continue


choose(0)