nums = [4, 9, 7, 5, 1]
target = 14
ans = []

def backtracking(start:int):
    if len(ans) == 2:
        if nums[ans[0]] + nums[ans[1]] == target:
            print(nums[ans[0]], nums[ans[1]])
            return ans
        return False

    for i in range(start+1, len(nums)):
        ans.append(i)
        if backtracking(start=i+1):
            return ans
        ans.pop()

backtracking(start=0)