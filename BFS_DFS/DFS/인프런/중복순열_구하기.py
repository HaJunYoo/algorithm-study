import sys

sys.stdin = open("in1.txt", "r")
input = sys.stdin.readline


def permutation(cnt, num):
    global res

    if cnt == m:
        res += 1
        print(num.strip())
        return

    for i in range(1, n + 1):
        permutation(cnt + 1, num + " " + str(i))


if __name__ == "__main__":
    n, m = map(int, input().split())

    res = 0

    permutation(0, "")
    print(res)
