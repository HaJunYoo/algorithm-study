n = int(input())

#1 2 4 8 16
#

def DFS(x):
    if x == 0:
        return

    else:
        print(x % 2, end=' ')  # x를 2로 나눈 나머지를 출력하고
        DFS(x // 2)  # 2를 나눈 몫을 다음 재귀로 넘겨준다

