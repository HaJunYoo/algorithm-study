from itertools import combinations

def solution(relation):
    col_len = len(relation[0])
    row_len = len(relation)

    candidate_keys = []
    for length in range(1, col_len + 1):
        for cols in combinations(range(col_len), length):
            # print(cols)
            minimality = True
            row_set = set()

            # print(candidate_keys)
            # 최소성 검사
            for key in candidate_keys:
                if set(key).issubset(set(cols)):
                    print(key, cols)
                    minimality = False
                    break
            if not minimality:
                continue

            # 유일성
            for r in range(row_len):
                row_str = ""
                for c in cols:
                    # print(r, c, relation[r][c])
                    row_str += relation[r][c]
                    # print(row_str)
                row_set.add(row_str)

            if len(row_set) == row_len:
                candidate_keys.append(cols)

    answer = len(candidate_keys)
    return answer


if __name__ == '__main__':
    relation = [["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]
    print(solution(relation))