from typing import List


class Solution:

    def partition(self, s: str) -> List[List[str]]:
        if len(s) == 0:
            return []

        def check_parlindrome(string):
            if string == string[::-1]:
                return True
            else:
                return False

        def dfs(s, start, subset, result):

            if start == len(s):
                result.append(subset[:])
                return

            for i in range(start + 1, len(s) + 1):
                tmp_str = s[start:i]
                if check_parlindrome(string=tmp_str):
                    subset.append(tmp_str)
                    dfs(s=s, start=i, subset=subset, result=result)
                    subset.pop()

        subset = []
        result = []
        dfs(s, 0, subset, result)

        return result



if __name__ == '__main__':
    s = "aab"
    solution = Solution()
    array = solution.partition(s=s)
    print(array)