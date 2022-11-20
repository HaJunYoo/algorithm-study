# import sys
#
# sys.stdin = open("in3.txt", "r")
# # 입력속도가 빨라짐
# input = sys.stdin.readline

def solve(array):
    global res

    temp = list()

    if len(array) < 2:
        # print(array[-1])
        res = array[-1]

    else:
        for i in range(len(array) - 1):
            temp.append(array[i] + array[i + 1])
        # print(temp)
        solve(temp)


def print_numbers():
    for elem in numbers:
        print(elem, end=" ")
    print()


def permutation(dep):
    if candidate:
        return

    # 트리의 깊이가 0 -> n에 도달하면
    if dep == n:
        solve(numbers)
        if res == f:
            print_numbers()
            candidate.append(numbers)
        return

    for i in range(1, n + 1):
        if not visited[i]:
            numbers.append(i)
            visited[i] = True
            permutation(dep + 1)

            numbers.pop()
            visited[i] = False


if __name__ == "__main__":
    n, f = map(int, input().split())
    numbers = []
    candidate = []
    visited = [False] * (n + 1)
    permutation(0)

    res = 0
