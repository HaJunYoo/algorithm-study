import sys
import math

sys.stdin = open("in1.txt", "r")
# 입력속도가 빨라짐
input = sys.stdin.readline

def solve():
    tmp = 0
    for a, b in zip(d, numbers):
        tmp += a * b
    return tmp

def print_numbers():
    for elem in numbers:
        print(elem, end=" ")
    print()

def permutation(dep):
    global res

    if candidate:
        return

    # 트리의 깊이가 0 -> n에 도달하면
    if dep == n:
        res = solve()
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
    d = [math.comb(n - 1, i) for i in range(n)]
    res = 0

    permutation(0)


