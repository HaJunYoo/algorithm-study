from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:

        def binary_search(start: int, end: int):
            if start > end:
                return -1

            mid = (start + end) // 2

            if nums[mid] == target:
                return mid

            if nums[mid] < target:
                return binary_search(start=mid+1, end=end)
            else:
                return binary_search(start=start, end=mid-1)

        return binary_search(start=0, end=len(nums)-1)

    def search2(self, nums, target):
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return -1  # 타겟이 배열에 없는 경우
