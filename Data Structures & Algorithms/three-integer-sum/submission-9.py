class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # keep track of 3 indices. 2 pointer with a 3rd fixed point
        
        ans = []
        nums = sorted(nums)
        
        for i in range(len(nums)):
            a = nums[i]
            if a > 0:
                return ans
            l = i + 1
            r = len(nums) - 1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum == 0:
                    if [a, nums[l], nums[r]] not in ans:
                        ans.append([a, nums[l], nums[r]])
                    l += 1
                elif threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
        return ans
                

