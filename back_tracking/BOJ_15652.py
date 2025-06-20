n, m = map(int, input().split())

numbers = list()

def print_numbers():
    for num in numbers:
        print(num, end = " ")
    print()

def choose(cnt, index):
    if cnt == m+1 :
        # 출력
        print_numbers()
        return

    for i in range(index, n+1):
        # 루프 인덱스를 뽑으려는 수의 인덱스 파라미터 인자로 넣어준다
        numbers.append(i)
        # print(numbers)
        choose(cnt+1, i)
        numbers.pop()

# index는 뽑으려는 수의 인덱스
# cnt => 뽑는 자리의 인덱스
choose(1, 1)
