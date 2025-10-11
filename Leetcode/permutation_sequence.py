from itertools import permutations

class Solution1:
    @staticmethod
    def getPermutation(n: int, k: int) -> str:
        
        candidates = [i for i in range(1, n+1)]
        cnt = 0
        res = ""
        for object in permutations(candidates, n):
            cnt += 1
            if cnt == k:
                for e in object:
                    res += str(e)
                break
        return res


if __name__ == '__main__':
    n = 3
    k = 3
    ans = Solution1.getPermutation(n, k)
    print(ans)