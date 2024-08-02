def solution(citations):
    citations.sort(reverse=True)
    for idx, cite in enumerate(citations, 1):
        # print(temp)
        # idx 는 최대 인용 횟수가 된다
        # 단일 논문의 인용 횟수 - 논문의 최대 인용 횟수
        # 위의 값이 음수가 되면 그 이전 인덱스가 바로 최대 인용 횟수 h index
        if cite - idx < 0:
             return idx - 1

    # 만약 꼭지점이 없었다면, 그 논문 전체 개수가 최대 인용 횟수가 될 수 있습니다
    return len(citations)


if __name__ == '__main__':
    citations = [3, 0, 6, 1, 5]
    print(solution(citations))
