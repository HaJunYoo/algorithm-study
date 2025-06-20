n, m = map(int, input().split())

numbers = list()

# 중복되지 않는 순열을 뽑기 위한 방문 확인 리스트
visited = [False]*(n+1)


def print_number():
    for num in numbers :
        print(num, end =" ")
    print()

def choose(cnt):

    if cnt == m :
        print_number()
        return

    for i in range(1, n+1):
        if not visited[i] :
            numbers.append(i)
            visited[i] = True
            choose(cnt+1)
            numbers.pop()
            visited[i] = False

        # 방문했다면 스킵
        else :
            continue


choose(0)