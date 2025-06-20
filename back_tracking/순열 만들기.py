n = int(input())

# 사용했던 숫자의 사용 여부를 담을 리스트
visited = [False] * (n + 1)
answer = []


def print_num():
    for elem in answer:
        print(elem, end=" ")
    # print(visited)
    print()


def permutation(index):
    if index == n + 1:
        print_num()
        return

    else:
        for i in range(1, n + 1):
            if visited[i]:
                continue

            visited[i] = True
            answer.append(i)

            permutation(index + 1)

            answer.pop()
            visited[i] = False


permutation(1)


# bool([False, False, False])