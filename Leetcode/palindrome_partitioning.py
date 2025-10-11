from typing import List

class Solution:
    
    @staticmethod
    def partition(s: str) -> List[List[str]]:
        if not s:
            return []
        lists = []
        partitions = []
        target_len = len(s)
        
        def backtrack(s, start, partitions, lists):
            
            tmp_str = ""
            if start == target_len:
                lists.append(partitions[:])
                return
            
            for i in range(start + 1, target_len + 1):
                tmp_str = s[start:i]
                if tmp_str == tmp_str[::-1]:
                    # 넣고 다음 인덱스로
                    partitions.append(tmp_str)
                    backtrack(s, i, partitions, lists)
                    # 넣은 부분 pop
                    partitions.pop()
        
        backtrack(s, 0, partitions, lists)
        
        return lists


if __name__ == '__main__':
    s = "aab"
    ans = Solution.partition(s)
    print(ans)