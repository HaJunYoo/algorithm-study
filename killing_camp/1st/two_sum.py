nums = [4, 9, 7, 5, 1]
target = 17
ans = []

def backtracking(start):
    if len(ans) == 3:
        # print(nums[ans[0]], nums[ans[1]])
        if nums[ans[0]] + nums[ans[1]] + nums[ans[2]] == target:
            print(ans)
            return ans
        return False

    for i in range(start, len(nums)):
        ans.append(i)
        if backtracking(i+1):
            return ans
        ans.pop()

backtracking(0)