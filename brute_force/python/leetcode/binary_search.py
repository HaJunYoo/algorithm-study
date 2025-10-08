from bisect import bisect_left
from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        idx = bisect_left(nums, target)
        
        # idx가 범위 내에 있고, 해당 위치의 값이 target과 같은지 확인
        if idx < len(nums) and nums[idx] == target:
            return idx
        
        return -1