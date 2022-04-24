class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxLength = 0
        memo = {}
        for i in range(len(nums)):
            maxLength = max(rec(nums, i, memo) + 1, maxLength)

        return maxLength

        # The cleaner method here
        # LIS = [1] * len(nums)
        # for i in reversed(range(len(nums)-1)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] < nums[j]:
        #             LIS[i] = max(LIS[i], LIS[j]+1)
        # return max(LIS)




def rec(nums, index, memo):
    if index in memo:
        return memo[index]
    if index >= len(nums) - 1:
        return 0

    depths = []

    for i in range(index + 1, len(nums)):
        if nums[index] < nums[i]:
            depths.append(rec(nums, i, memo) + 1)

    if len(depths) == 0:
        memo[index] = 0
    else:
        memo[index] = max(depths)

    return memo[index]



