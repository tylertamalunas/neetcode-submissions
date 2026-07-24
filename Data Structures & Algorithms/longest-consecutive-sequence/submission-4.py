class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # no sorting
        # convert to hash set, then only look at numbers without n-1 in the array
        # store a max and a current max, replace max with new max if higher

        nset = set(nums)
        longest = 0

        for num in nset:
            length = 1
            if num - 1 in nset:
                continue
            while num + length in nset:
                length += 1
            longest = max(length, longest)
        
        return longest