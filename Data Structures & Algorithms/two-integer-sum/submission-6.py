class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = []

        for num in range(len(nums)):
            val = target - nums[num]
            if val in hm:
                return [hm.index(val), num]
            else:
                hm.append(nums[num])
