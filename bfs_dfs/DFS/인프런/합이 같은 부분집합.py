"""
입력 :
- 6
- 1 3 5 6 7 10

출력 :  YES

- 5
- 1 5 6 7 10

"""
import sys

n = int(input())

a = list(map(int, input().split()))

total = sum(a)


def DFS(L, sum):
    if L == n:
        if sum == (total - sum):
            print("yes")
            sys.exit(0)  # 아예 프로그램을 종료 -> process finished with exit code 0

    else:
        DFS(L + 1, sum + a[L])  # L번 인덱스의 원소를 합하겠다
        DFS(L + 1, sum)  # L번 인덱스의 원소를 합하지 않겠다.


DFS(0, 0)

print("No") # 프로그램이 종료된 후 해당 라인을 실행