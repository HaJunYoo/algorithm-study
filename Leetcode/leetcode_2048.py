from collections import Counter

class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        def is_balanced(num: int) -> bool:
            s = str(num)
            cnt = Counter(s)
            for digit, c in cnt.items():
                if int(digit) != c:
                    return False
            return True

        cur = n + 1
        while True:
            if is_balanced(cur):
                return cur
            cur += 1

### ----

class Solution2:
    def nextBeautifulNumber(self, n: int) -> int:
        res = set()

        def backtrack(digit: int, cur: list):
            # digit = 현재 고려할 숫자 (1~7)
            if digit > 7:  # 7 넘어가면 종료
                num = int("".join(cur))
                res.add(num)
                return
            # case 1: 현재 digit 사용 안 함
            backtrack(digit + 1, cur)

            # case 2: 현재 digit 사용 (digit번 추가)
            new_cur = cur + [str(digit)] * digit
            backtrack(digit + 1, new_cur)

        backtrack(1, [])

        # 모든 후보 중 n보다 큰 것 중 최소값
        candidates = sorted([x for x in res if x > n])
        return candidates[0]