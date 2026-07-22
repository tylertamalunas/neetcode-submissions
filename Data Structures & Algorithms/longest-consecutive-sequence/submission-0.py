class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # brute is just sort, but then O(nlogn) so no deal
        # convert to a set so we can lookup in O(1)
        # only have to track nums that do not have num-1 in the set


        # edges
        if len(nums) == 0 or len(nums) == 1:
            return len(nums)
        
        nset = set(nums)
        longest = 0

        for num in nset:
            if (num - 1) not in nset:
                length = 1
                while (num + length) in nset:
                    length += 1
                if length > longest:
                    longest = length
        
        return longest
        
        