class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        holder = {}

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in holder:
                return [holder[diff], i]
            holder[nums[i]] = i