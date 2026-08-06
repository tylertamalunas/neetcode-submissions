class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # hash map, key is array value?
        nums_map = defaultdict(map)

        for i in range(len(nums)):
            sum = target - nums[i]
            if sum in nums_map:
                return [nums_map.get(sum), i]
            nums_map[nums[i]] = i
        return []