import sys

sys.stdin = open("in1.txt", "r")
# 입력속도가 빨라짐
input = sys.stdin.readline


def permutation(cnt):
    global res

    if cnt == m:
        res += 1

        for elem in numbers:
            print(elem, end=' ')
        print()

        return

    else:
        for i in range(1, n+1):
            if not visited[i]:
                numbers.append(i)
                visited[i] = True
                permutation(cnt+1)
                visited[i] = False
                numbers.pop()
            else:
                continue



if __name__ == "__main__":

    n, m = map(int, input().split())
    visited = [False] * (n + 1)
    numbers = []

    res = 0

    permutation(0)
    print(res)

