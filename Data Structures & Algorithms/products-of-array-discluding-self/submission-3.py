class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # prefix and postfix, 
        ans = [1] * (len(nums))

        prefix = 1
        for i in range(len(nums)):
            ans[i] = prefix
            prefix *= nums[i]
        
        postfix = 1
        for n in range(len(nums) - 1, -1, -1):
            ans[n] *= postfix
            postfix *= nums[n]

        return ans

