class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #presum postsum
        result = [1] * len(nums)

        presum = 1
        for i in range(len(nums)):
            result[i] = presum
            presum *= nums[i]

        postsum = 1
        for k in range(len(nums) - 1, -1, -1):
            result[k] *= postsum
            postsum *= nums[k]

        return result

