def solution(storey):
    answer = 0

    while storey:
        digit = storey % 10
        next_digit = (storey // 10) % 10

        # 현재 자릿수가 5보다 크다면 10으로 올리는 편이 나음
        # 현재 자릿수가 5이지만, 다음 자릿수가 5이상일 때
        if digit > 5 or (digit == 5 and next_digit >= 5):
            # 10의 자릿수로 올리기 위한 클릭수
            answer += (10 - digit)
            # 10의 자리를 한번 올림
            storey += 10
        else:
            # 그렇지 않으면 해당 자릿수 * -1을 눌러서 내리는 것이 빠름
            answer += digit

        # 10으로 나눈 몫
        storey //= 10

    return answer