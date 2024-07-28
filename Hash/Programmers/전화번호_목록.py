def solution(phone_book):
    phone_book.sort()  # 전화번호부를 정렬합니다. (그리디 접근)

    for i in range(len(phone_book) - 1):
        if phone_book[i + 1].startswith(phone_book[i]):
            return False

    return True


# ------------------------------------------------------


def solution(phone_book):
    phone_book.sort()  # 전화번호부를 정렬합니다.

    for i in range(len(phone_book) - 1):
        len_1 = len(phone_book[i])
        if phone_book[i + 1][:len_1] == phone_book[i]:
            return False

    return True

# ------------------------------------------------------

def solution(phone_book):
    prefix_map = {}
    phone_book.sort(key=lambda x: len(x))

    for idx, phone_number in enumerate(phone_book):
        for i in range(len(phone_number)):
            prefix = phone_number[:i]
            if prefix in prefix_map:
                return False

        if phone_number in prefix_map:
            return False

        prefix_map[phone_number] = phone_number

    return True