class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # PREFIX SUM METHOD
        # calculate prefix, of all
        # find postfix and adjust array 
        ans = [1] * (len(nums))

        prefix = 1
        for i in range(len(nums)):
            ans[i] = prefix
            prefix *= nums[i]

        postfix = 1
        for j in range(len(nums) - 1, -1, -1):
            ans[j] *= postfix
            postfix *= nums[j]

        return ans
