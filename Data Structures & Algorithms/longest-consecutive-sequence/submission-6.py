class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # only start counting at numbers that do not have a number lower than it. 
        # convert to set for O(1) lookups
        # need an outside max and inside counter

        working = set(nums)
        highest = 0
        for num in working:
            count = 1
            if (num - 1) in working:
                continue
            while num + count in working:
                count += 1
            highest = max(count, highest)
        
        return highest

