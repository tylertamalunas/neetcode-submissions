class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # presum postsum
        # create array of presums, then do postsums in reverse order to replace presums

        ans = [1] * len(nums)

        presum = 1
        for i in range(len(nums)):
            ans[i] = presum
            presum *= nums[i]

        postsum = 1
        for j in range(len(nums) - 1, -1, -1):
            ans[j] *= postsum
            postsum *= nums[j]

        return ans