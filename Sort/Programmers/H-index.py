def solution(citations):
    citations.sort(reverse=True)
    for idx, cite in enumerate(citations, 1):
        # print(temp)
        if cite - idx < 0:
             return idx - 1

    return len(citations)


if __name__ == '__main__':
    citations = [3, 0, 6, 1, 5]
    print(solution(citations))
