nums = [4, 9, 7, 5, 1]
target = 17
ans = []

def twosum():
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            for k in range(j+1, len(nums)):
                if nums[i] + nums[j] + nums[k] == target:
                    print(f'two sum : {i}, {j}, {k}')
                    return [i, j, k]


def backtracking(start):
    if len(ans) == 3:
        # print(nums[ans[0]], nums[ans[1]])
        if nums[ans[0]] + nums[ans[1]] + nums[ans[2]] == target:
            print(f'back tracking : {ans}')
            return ans
        return False

    for i in range(start, len(nums)):
        ans.append(i)
        if backtracking(i+1):
            return ans
        ans.pop()

twosum()
backtracking(0)