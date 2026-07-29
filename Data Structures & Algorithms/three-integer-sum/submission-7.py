class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # need a anchor index, then 2 pointers

        ans = []
        nums.sort()

        for i in range(len(nums)):
            a = nums[i]
            if a > 0:
                break
            l = i + 1
            r = len(nums) - 1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                if threeSum == 0:
                    if [a, nums[l], nums[r]] not in ans:
                        ans.append([a, nums[l], nums[r]])
                    l += 1
                    r -= 1
        return ans
                    
            