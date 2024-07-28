from collections import defaultdict


def solution(clothes):
    answer = 1

    # 타입 별 옷의 개수를 계산
    clothes_hash = defaultdict(int)
    for clothe in clothes:
        c, type = clothe
        clothes_hash[type] += 1

    # 옷 입는 패턴에 대한 경우의 수를 계산
    for key, val in clothes_hash.items():
        answer *= (val + 1)

    # 옷을 안 입는 경우를 제거
    return answer - 1