from itertools import combinations, permutations


# import collections

# 0은 소수가 아님
# 만들어진 순열에 대해서 소수 판별
def solution(numbers):
    answer = 0
    v = [str(num) for num in numbers]

    # 숫자 조합 만드는 부분 => 순열로 생성
    v_2 = []
    for i in range(1, len(v) + 1):
        for string in permutations(v, i):
            str_num = list(string)
            # print(str_num)
            int_num = int(''.join(str_num))
            # print(int_num)
            if int_num > 0 and int_num not in v_2:
                v_2.append(int_num)

    v_2 = set(v_2)
    v_2 = list(v_2)

    # 만들어진 조합 중 제일 큰 수
    max_len = max(v_2)

    # max_len까지의 소수 체크
    # 소수가 아니면 False
    visited = [False] * (max_len + 1)
    for j in range(2, (max_len + 1) // 2):
        # j부터 배수로 필터링
        # visited에 체크
        if visited[j]:
            continue
        # 2는 소수 => 2*2(4)부터 소수가 아님
        else:
            for k in range(j * 2, max_len + 1, j):
                visited[k] = True

            # 소수들만 리스트 만듦
    odd = []
    for l in range(2, max_len + 1):
        if not visited[l]:
            # print(l, end= ' ')
            odd.append(l)

    # print(odd)
    # 만들어진 숫자 조합이 만약 소수 안에 있으면 cnt 올리기
    cnt = 0
    for o_num in v_2:
        if o_num in odd:
            # print(o_num)
            cnt += 1

    print(cnt)
    return cnt