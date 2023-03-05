def solution(brown, yellow):

    total = brown + yellow

    m, n = 0, 0

    for i in range(1, total + 1):
        if total % i == 0:
            m1 = i
            n1 = total // m1
            if m1 >= n1:
                n2 = brown / 2 - m1 + 2

                if n2 == n1:
                    m = m1
                    n = n1

    print(f'{m} {n}')

    answer = [m, n]

    return answer